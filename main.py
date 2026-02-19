from nicegui import ui

ui.add_head_html(
    '''
<style>
    body {
        margin: 0;
        background: #f7f7f8;
        color: #1f2937;
        font-family: Inter, "PingFang SC", "Microsoft YaHei", sans-serif;
    }
    .app-shell {
        min-height: 100vh;
        width: 100%;
        gap: 0;
    }
    .sidebar {
        width: 240px;
        min-height: 100vh;
        background: #efeff1;
        border-right: 1px solid #e1e3e7;
        padding: 14px 10px;
        gap: 8px;
    }
    .brand {
        font-size: 18px;
        font-weight: 700;
        color: #111827;
        padding: 8px 10px 14px 10px;
    }
    .nav-link {
        display: block;
        text-decoration: none;
        color: #1f2937 !important;
        padding: 10px 12px;
        border-radius: 10px;
        font-size: 15px;
        font-weight: 500;
        transition: background .2s ease;
    }
    .nav-link:hover {
        background: #e5e7eb;
    }
    .nav-link.active {
        background: #e5e7eb;
        font-weight: 700;
    }
    .main {
        flex: 1;
        min-height: 100vh;
        padding: 18px 24px;
        background: #f7f7f8;
    }
    .topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 120px;
    }
    .top-title {
        font-size: 30px;
        font-weight: 700;
    }
    .page-center {
        width: 100%;
        max-width: 820px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 26px;
    }
    .hero-title {
        font-size: 44px;
        font-weight: 700;
        color: #111827;
    }
    .hero-desc {
        font-size: 16px;
        color: #6b7280;
        margin-top: -12px;
    }
    .prompt-box {
        width: 100%;
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 28px;
        padding: 12px 18px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
    }
    .prompt-left {
        color: #9ca3af;
        font-size: 16px;
    }
    .pill {
        background: #eef2ff;
        color: #4338ca;
        font-size: 12px;
        padding: 6px 10px;
        border-radius: 999px;
        font-weight: 600;
    }
</style>
''',
    shared=True,
)


def render_layout(active_path: str, title: str, description: str) -> None:
    with ui.row().classes('app-shell'):
        with ui.column().classes('sidebar'):
            ui.label('AI绘图').classes('brand')
            links = [
                ('首页', '/'),
                ('图片管理', '/images'),
                ('工作流编辑页面', '/workflow'),
                ('设置页面', '/settings'),
            ]
            for text, path in links:
                classes = 'nav-link active' if path == active_path else 'nav-link'
                ui.link(text, path).classes(classes)

        with ui.column().classes('main'):
            with ui.row().classes('topbar w-full'):
                ui.label(title).classes('top-title')
                ui.label('AI绘图 Plus').classes('pill')

            with ui.column().classes('page-center'):
                ui.label('今天想创作什么？').classes('hero-title')
                ui.label(description).classes('hero-desc')
                with ui.row().classes('prompt-box'):
                    ui.label('＋ 输入你的需求，例如：赛博朋克城市夜景').classes('prompt-left')
                    ui.label('开始').classes('pill')


@ui.page('/')
def home_page() -> None:
    render_layout('/', '首页', '描述你的想法，快速生成第一张 AI 图片。')


@ui.page('/images')
def image_page() -> None:
    render_layout('/images', '图片管理', '管理历史生成结果，筛选、预览和归档作品。')


@ui.page('/workflow')
def workflow_page() -> None:
    render_layout('/workflow', '工作流编辑页面', '配置模型、参数与节点，打造你的自动化创作流程。')


@ui.page('/settings')
def settings_page() -> None:
    render_layout('/settings', '设置页面', '调整系统偏好、默认分辨率与生成质量选项。')


ui.run(title='AI绘图', port=8080)
