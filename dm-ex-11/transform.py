import glob
import pandas
import os
import dateutil


# get paths
def get_paths(type):
    if type == 'csv':
        path = 'sources\\*.csv'
        return [f for f in glob.glob(path, recursive=True)]
    elif type == 'json':
        path = 'unautomated sources\\*.json'
        return [f for f in glob.glob(path, recursive=True)]
    else:
        print('wrong argument, csv or json expected')

# get country code
def get_country_code(filename, typefile):
    if typefile == 'csv':
        return filename[-13:-11]
    elif typefile == 'json':
        return filename[20:22]
    else:
        print('wrong argument, csv or json expected')


# transform files (adding columns, split date)
def prepare_trending_videos():
    files = get_paths('csv')
    frames = []

    for f in files: # For each source file
        code = get_country_code(f, 'csv')
        publish_time = ''
        publish_date = ''

        file = pandas.read_csv(f)
        for i, row in file.iterrows():
            d = dateutil.parser.parse(row['publishedAt'])
            publish_date = d.strftime('%Y-%d-%m')
            publish_time = d.strftime('%H:%M:%S')

        file.insert(16, 'country_code', code)
        file.insert(17, 'publish_time', publish_time)
        file.insert(18, 'publish_date', publish_date)
        file.drop("publishedAt", axis=1, inplace=True)
        frames.append(file)

    if not os.path.exists("transformed files/"):
        os.mkdir("transformed files/")

    combined_csv = pandas.concat(frames, ignore_index=True)
    print('writing combined csv ...')
    combined_csv.to_csv(
        r"transformed files/trending_videos.csv", 
        encoding='utf-8-sig', 
        header=True, 
        index=True, 
        index_label="trending_videos_id")


# Split tags
def prepare_tags():
    src = pandas.read_csv('transformed files/trending_videos.csv') # source file
    tab = []

    for i, row in src.iterrows():
        tags = row['tags'].split('|')
        for tag in tags:
            tab.append([tag, row['trending_videos_id']])

    print("writing videos_tags.csv ...")
    dtn = pandas.DataFrame(tab, columns=['tag_name', 'trending_videos_id'])
    dtn.to_csv(
        r"transformed files/videos_tags.csv",
        encoding='utf-8-sig',
        index=True,
        index_label="video_tags_id")


# prepare categories
def prepare_categories():
    files = get_paths('json')
    rows = []
    for f in files:
        code = get_country_code(f, 'json')
        file = pandas.read_json(f)
        for i in file['items']:
            rows.append([i['id'], code, i['snippet']['title'], i['etag']])
    
    print("writing videos_categories.csv ...")
    dtn = pandas.DataFrame(rows, columns=['categoryId', 'country_code', 'title', 'etag'])
    dtn.to_csv(
        r"transformed files/videos_categories.csv",
        encoding='utf-8-sig',
        index=False
    )

if __name__ == '__main__':
    prepare_trending_videos()
    prepare_tags()
    prepare_categories()
