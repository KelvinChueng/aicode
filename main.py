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
    .app-shell { min-height: 100vh; width: 100%; gap: 0; }
    .sidebar {
        width: 240px; min-height: 100vh; background: #efeff1; border-right: 1px solid #e1e3e7;
        padding: 14px 10px; gap: 8px;
    }
    .brand { font-size: 20px; font-weight: 700; color: #111827; padding: 4px 10px 10px; }
    .nav-link {
        display: block; text-decoration: none; color: #1f2937 !important; padding: 10px 12px;
        border-radius: 10px; font-size: 15px; font-weight: 500; transition: background .2s ease;
    }
    .nav-link:hover { background: #e5e7eb; }
    .nav-link.active { background: #e5e7eb; font-weight: 700; }
    .main { flex: 1; min-height: 100vh; padding: 18px 24px; background: #f7f7f8; }
    .topbar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 120px; }
    .top-title { font-size: 30px; font-weight: 700; }
    .page-center {
        width: 100%; max-width: 820px; margin: 0 auto; display: flex; flex-direction: column;
        align-items: center; gap: 26px;
    }
    .hero-title { font-size: 44px; font-weight: 700; color: #111827; }
    .hero-desc { font-size: 16px; color: #6b7280; margin-top: -12px; }
    .prompt-box {
        width: 100%; background: #ffffff; border: 1px solid #e5e7eb; border-radius: 28px;
        padding: 12px 18px; display: flex; align-items: center; justify-content: space-between;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
    }
    .prompt-left { color: #9ca3af; font-size: 16px; }
    .pill { background: #eef2ff; color: #4338ca; font-size: 12px; padding: 6px 10px; border-radius: 999px; font-weight: 600; }

    .q-shell { min-height: 100vh; width: 100%; gap: 0; background: #f4f5f7; }
    .q-side {
        width: 250px; background: #f1f2f4; border-right: 1px solid #e2e5ea; min-height: 100vh;
        padding: 12px 10px; gap: 8px;
    }
    .q-logo { font-size: 34px; font-weight: 900; color: #4f46e5; line-height: 1; padding: 0 8px; }
    .q-brand { font-size: 28px; font-weight: 800; color: #111827; margin-top: -8px; padding: 0 8px 6px; }
    .q-btn { background: #e6e8ec; border: 1px solid #d8dce3; border-radius: 10px; padding: 8px 12px; font-weight: 700; }
    .q-group-title { color: #9ca3af; font-size: 13px; padding: 8px 8px 0; }
    .q-item { color: #4b5563; font-size: 14px; padding: 7px 8px; border-radius: 8px; }
    .q-item:hover { background: #e6e8ec; }

    .q-main { flex: 1; min-height: 100vh; padding: 14px 22px; }
    .q-top { display: flex; justify-content: space-between; align-items: center; color: #475569; margin-bottom: 115px; }
    .q-model { font-size: 34px; font-weight: 700; color: #1f2937; }
    .q-actions { font-size: 14px; color: #6b7280; }
    .q-center { max-width: 760px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; gap: 24px; }
    .q-title { font-size: 52px; font-weight: 700; color: #1f2940; margin-top: 70px; }
    .q-input {
        width: 100%; background: #fff; border: 1px solid #d9dee5; border-radius: 28px;
        box-shadow: 0 2px 10px rgba(15, 23, 42, 0.05); padding: 16px 18px 10px;
    }
    .q-ph { color: #c1c7d0; font-size: 30px; margin-bottom: 16px; }
    .q-tools { display: flex; align-items: center; justify-content: space-between; }
    .q-tools-left { display: flex; gap: 8px; flex-wrap: wrap; }
    .q-chip {
        background: #f5f6f8; color: #6b7280; border: 1px solid #eceff3; border-radius: 14px;
        padding: 6px 10px; font-size: 12px;
    }
    .q-send { background: #c7d2fe; color: #4f46e5; border-radius: 999px; padding: 7px 10px; font-weight: 700; }
    .q-tools-grid { display: flex; gap: 44px; margin-top: 26px; }
    .q-tool { text-align: center; color: #6b7280; font-size: 14px; }
    .q-icon { font-size: 26px; line-height: 1.2; margin-bottom: 6px; }
</style>
''',
    shared=True,
)


def render_sidebar(active_path: str) -> None:
    with ui.column().classes('sidebar'):
        ui.label('AI绘图').classes('brand')
        links = [('首页', '/'), ('图片管理', '/images'), ('工作流编辑页面', '/workflow'), ('设置页面', '/settings')]
        for text, path in links:
            classes = 'nav-link active' if path == active_path else 'nav-link'
            ui.link(text, path).classes(classes)


def render_layout(active_path: str, title: str, description: str) -> None:
    with ui.row().classes('app-shell'):
        render_sidebar(active_path)
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


def render_settings_like_reference() -> None:
    with ui.row().classes('q-shell'):
        with ui.column().classes('q-side'):
            ui.label('✦').classes('q-logo')
            ui.label('千问').classes('q-brand')
            ui.button('✎ 新对话').classes('q-btn')
            ui.label('对话分组').classes('q-group-title')
            for item in [
                '反推-image-turbo提示词', '小红书网球女孩提示词', '4xFFHQDAT：人像AI放大模型', 'Python',
                'ComfyUI报错：安全级别限制操作', '下载qwen_3_8b_fp8mixed权重', '解决ComfyUI中缺少节点的问题',
            ]:
                ui.label(item).classes('q-item')

        with ui.column().classes('q-main'):
            with ui.row().classes('q-top w-full'):
                ui.label('Qwen3.5- Plus ⌄').classes('q-model')
                ui.label('下载电脑版   API 服务   ◔').classes('q-actions')

            with ui.column().classes('q-center'):
                ui.label('你好，我是千问').classes('q-title')
                with ui.column().classes('q-input'):
                    ui.label('向千问提问').classes('q-ph')
                    with ui.row().classes('q-tools'):
                        with ui.row().classes('q-tools-left'):
                            for chip in ['任务助理', '深度思考', '深度研究', '代码', '图像', '更多']:
                                ui.label(chip).classes('q-chip')
                        ui.label('↑').classes('q-send')

                with ui.row().classes('q-tools-grid'):
                    for icon, text in [('🎙', '录音'), ('🖼', 'PPT'), ('▶', '音视频'), ('📄', '文档'), ('◼', '发现')]:
                        with ui.column().classes('q-tool'):
                            ui.label(icon).classes('q-icon')
                            ui.label(text)


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
    render_settings_like_reference()


ui.run(title='AI绘图', port=8080)
