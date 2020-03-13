import sqlite3
import pandas


# load the trending videos in the database
def push_trending_videos():
    try:
        conn = sqlite3.connect('db/DB-TRENDING-VIDEOS-G11.db')
        c = conn.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS TRENDING_VIDEOS (
                [trending_videos_id] INTEGER PRIMARY KEY,
                [country_code] TEXT,
                [video_id] TEXT,
                [trending_date] TEXT,
                [title] TEXT,
                [publish_time] TEXT,
                [publish_date] TEXT,
                [categoryId] INTEGER,
                [channeltitle] TEXT,
                [channelId] TEXT,
                [view_count] INTEGER,
                [likes] INTEGER,
                [dislikes] INTEGER,
                [comment_count] INTEGER,
                [thumbnail_link] TEXT,
                [comments_disabled] TEXT,
                [ratings_disabled] TEXT,
                [video_error_or_removed] TEXT,
                [description] TEXT,
                [tags] TEXT
            )
            """
        )
        reader = pandas.read_csv('transformed files/trending_videos.csv')
        reader.to_sql('TRENDING_VIDEOS', conn, if_exists='append', index=False)
        conn.commit()
    except Exception as error:
        print('database error : ' + str(error))
    finally:
        conn.close()


# load the video tags in the database
def push_videos_tags():
    try:
        conn = sqlite3.connect('db/DB-TRENDING-VIDEOS-G11.db')
        c = conn.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS VIDEOS_TAGS (
                [video_tags_id] INTEGER PRIMARY KEY,
                [tag_name] TEXT,
                [trending_videos_id] INTEGER
            )
            """
        )
        reader = pandas.read_csv('transformed files/videos_tags.csv')
        reader.to_sql('VIDEOS_TAGS', conn, if_exists='append', index=False)
        conn.commit()
    except Exception as error:
        print('database error : ' + str(error))
    finally:
        conn.close()


# load the categories in the database
def push_videos_categories():
    try:
        conn = sqlite3.connect('db/DB-TRENDING-VIDEOS-G11.db')
        c = conn.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS VIDEOS_CATEGORIES (
                [categoryId] INTEGER,
                [country_code] TEXT,
                [title] TEXT,
                [etag] TEXT,
                PRIMARY KEY (categoryId, country_code)
            )
            """
        )
        reader = pandas.read_csv('transformed files/videos_categories.csv')
        reader.to_sql('VIDEOS_CATEGORIES', conn, if_exists='append', index=False)
        conn.commit()
    except Exception as error:
        print('database error : ' + str(error))
    finally:
        conn.close()


if __name__ == '__main__':
    push_trending_videos()
    push_videos_tags()
    push_videos_categories()
