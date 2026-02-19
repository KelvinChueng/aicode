from nicegui import ui


def render_nav() -> None:
    with ui.row().classes('w-full gap-2 p-4 bg-gray-100'):
        ui.link('首页', '/').classes('text-blue-600')
        ui.link('图片管理', '/images').classes('text-blue-600')
        ui.link('工作流编辑页面', '/workflow').classes('text-blue-600')
        ui.link('设置页面', '/settings').classes('text-blue-600')


@ui.page('/')
def home_page() -> None:
    render_nav()
    ui.label('首页').classes('text-2xl font-bold p-4')
    ui.label('欢迎使用 AI绘图').classes('px-4')


@ui.page('/images')
def image_management_page() -> None:
    render_nav()
    ui.label('图片管理').classes('text-2xl font-bold p-4')
    ui.label('在这里查看、上传和整理图片素材。').classes('px-4')


@ui.page('/workflow')
def workflow_editor_page() -> None:
    render_nav()
    ui.label('工作流编辑页面').classes('text-2xl font-bold p-4')
    ui.label('在这里编排绘图流程与节点。').classes('px-4')


@ui.page('/settings')
def settings_page() -> None:
    render_nav()
    ui.label('设置页面').classes('text-2xl font-bold p-4')
    ui.label('在这里修改系统参数和偏好。').classes('px-4')


ui.run(title='AI绘图', port=8080)
