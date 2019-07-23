from flask_bootstrap import Bootstrap
from flask_cache import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# 创建sqlalchemy对象
db = SQLAlchemy()
# 创建Migrate数据库迁移对象
migrate = Migrate()
# 创建Cache对象，CACHE_TYPE参数有：
# null: NullCache (default)
# simple: SimpleCache
# memcached: MemcachedCache (pylibmc or memcache required)
# gaememcached: GAEMemcachedCache
# redis: RedisCache (Werkzeug 0.7 required)
# filesystem: FileSystemCache
# saslmemcached: SASLMemcachedCache (pylibmc required)
cache = Cache(config={
    'CACHE_TYPE':'redis',
    'CACHE_KEY_PREFIX':'python'
})

def init_ext(app):
    # 初始化db
    db.init_app(app=app)
    # 初始化migrate
    migrate.init_app(app=app, db=db)
    # 初始化bootstrap对象，不需要在其他地方设置
    Bootstrap(app)
    # 初始化调试工具栏工具,debugtoolbar,不需要在其他地方设置
    DebugToolbarExtension(app)
    # 初始化缓存，flask-cache
    cache.init_app(app=app)

