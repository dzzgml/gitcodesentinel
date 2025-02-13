from core.repo_manager import RepoManager
from core.updater import Updater
from core.notifier import Notifier
from core.report_generator import ReportGenerator
from apscheduler.schedulers.blocking import BlockingScheduler

# 加载配置
config = Config()

# 初始化模块
repo_manager = RepoManager()
updater = Updater()
notifier = Notifier()
report_generator = ReportGenerator()

# 启动定时任务
scheduler = BlockingScheduler()
scheduler.add_job(updater.check_for_new_activity, 'interval', hours=1, args=[repo_manager.repositories])

scheduler.start()
