try:
    from gimpfu import *
except ImportError:
    from mock_gimpfu import *
from gimpfu_signatures import *  # comment on release

def create_xcf_file():
    # 创建一个新的图像
    img = gimp.Image(42 * 300 // 2.54, 29.7 * 300 // 2.54, RGB)
    img.resolution = (300, 300)

    # 创建背景图层并填充白色
    bg_layer = gimp.Layer(img, "Background", img.width, img.height, RGB_IMAGE, 100, NORMAL_MODE)
    pdb.gimp_context_set_background((255, 255, 255))
    bg_layer.fill(BACKGROUND_FILL)
    img.add_layer(bg_layer, 0)

    # 添加边框
    border_layer = gimp.Layer(img, "Border", img.width, img.height, RGB_IMAGE, 100, NORMAL_MODE)
    border_layer.fill(BACKGROUND_FILL)
    pdb.gimp_image_select_rectangle(img, CHANNEL_OP_REPLACE, 12, 12, img.width - 24, img.height - 24)
    pdb.gimp_edit_stroke(border_layer)
    img.add_layer(border_layer, 1)

    # 计算有效区域
    effective_width = img.width - 2.2 * 300 // 2.54 * 2 - 1.8 * 300 // 2.54
    effective_height = img.height - 3 * 300 // 2.54 - 2.2 * 300 // 2.54

    # 添加主标题
    text_layer = pdb.gimp_text_fontname(img, None, (img.width - effective_width) // 2, 3 * 300 // 2.54 + 1, "主标题", 0, True, 30, 0, "小标宋")
    img.add_layer(text_layer, 2)

    # 添加右侧索引标题
    index_text_layer = pdb.gimp_text_fontname(img, None, img.width - 0.5 * 300 // 2.54, 0.5 * 300 // 2.54, "索引标题内容", 0, True, 14, 90, "黑体")
    img.add_layer(index_text_layer, 3)

    # 添加右下角落款
    credit_text_layer = pdb.gimp_text_fontname(img, None, img.width - 0.5 * 300 // 2.54, img.height - 0.5 * 300 // 2.54, "XXXXXX 制", 0, True, 12, 0, "黑体")
    img.add_layer(credit_text_layer, 4)

    # 添加图例
    legend_text_layer = pdb.gimp_text_fontname(img, None, img.width - 2.2 * 300 // 2.54 - 50, img.height - 2.2 * 300 // 2.54 - 50, "图例", 0, True, 9, 0, "黑体")
    img.add_layer(legend_text_layer, 5)

    # 添加指北针
    north_text_layer = pdb.gimp_text_fontname(img, None, img.width - 1.8 * 300 // 2.54 - 20, 20, "北", 0, True, 20, 0, "黑体")
    img.add_layer(north_text_layer, 6)

    # 添加组织指挥列表（示例内容，可根据实际情况修改）
    list_text_layer = pdb.gimp_text_fontname(img, None, 2.2 * 300 // 2.54, img.height - 2.2 * 300 // 2.54 - 100, "总指挥：XXX\n副总指挥：XXX\n成员：XXX", 0, True, 10, 0, "黑体")
    img.add_layer(list_text_layer, 7)

    # 保存为 XCF 文件
    pdb.gimp_xcf_save(0, img, None, "output.xcf", "output.xcf")

    # 清理
    pdb.gimp_displays_flush()

register(
    "python-fu-create-xcf",
    "Create XCF file with specific layout",
    "Creates an XCF file with specific layout as described",
    "LyndonHu",
    "LyndonHu",
    "2024",
    "Create XCF",
    "",
    [],
    [],
    create_xcf_file
)

main()
