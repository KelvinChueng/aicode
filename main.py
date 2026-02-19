from nicegui import ui

ui.add_head_html(
    '''
<style>
    body {
        background: radial-gradient(circle at 20% 20%, #1a2a6c 0%, #0b1020 45%, #05070f 100%);
        color: #e6f1ff;
    }
    .glass-panel {
        background: linear-gradient(135deg, rgba(20, 30, 60, 0.82), rgba(8, 14, 30, 0.72));
        border: 1px solid rgba(97, 218, 251, 0.30);
        box-shadow: 0 0 24px rgba(97, 218, 251, 0.15), inset 0 0 24px rgba(97, 218, 251, 0.08);
        border-radius: 18px;
        backdrop-filter: blur(8px);
    }
    .neon-link {
        color: #79d7ff !important;
        text-decoration: none;
        font-weight: 700;
        padding: 10px 16px;
        border-radius: 12px;
        border: 1px solid rgba(121, 215, 255, 0.25);
        transition: all .2s ease;
        background: rgba(121, 215, 255, 0.06);
    }
    .neon-link:hover {
        color: #b6ecff !important;
        box-shadow: 0 0 14px rgba(121, 215, 255, 0.55);
        transform: translateY(-1px);
        background: rgba(121, 215, 255, 0.14);
    }
    .page-title {
        color: #c4eeff;
        text-shadow: 0 0 12px rgba(106, 214, 255, 0.55);
    }
    .muted {
        color: #9eb7cf;
    }
</style>
''',
    shared=True,
)


def render_shell(title: str, desc: str) -> None:
    with ui.column().classes('w-full min-h-screen p-6 md:p-10 gap-6'):
        ui.label('AI绘图控制台').classes('text-3xl font-black tracking-wide page-title')

        with ui.row().classes('glass-panel w-full items-center gap-3 p-3 md:p-4'):
            ui.link('首页', '/').classes('neon-link')
            ui.link('图片管理', '/images').classes('neon-link')
            ui.link('工作流编辑页面', '/workflow').classes('neon-link')
            ui.link('设置页面', '/settings').classes('neon-link')

        with ui.column().classes('glass-panel w-full p-6 md:p-8 gap-4'):
            ui.label(title).classes('text-3xl font-bold page-title')
            ui.label(desc).classes('text-lg muted')


@ui.page('/')
def home_page() -> None:
    render_shell('首页', '欢迎进入 AI 绘图平台，快速开始你的创作任务。')


@ui.page('/images')
def image_management_page() -> None:
    render_shell('图片管理', '集中管理上传图片、素材库和历史生成结果。')


@ui.page('/workflow')
def workflow_editor_page() -> None:
    render_shell('工作流编辑页面', '通过节点与参数编排你的智能绘图工作流。')


@ui.page('/settings')
def settings_page() -> None:
    render_shell('设置页面', '配置模型偏好、系统参数和界面选项。')


ui.run(title='AI绘图', port=8080)
