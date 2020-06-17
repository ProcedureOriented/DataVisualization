#第一组关键词Map地理位置图及热力图绘制代码
collect=[('河北', 25), ('山西', 32), ('江苏', 27), ('浙江', 38), ('安徽', 28), ('福建', 19), ('江西', 18), ('河南', 35), ('湖北', 55), ('湖南', 65), ('海南', 37), ('陕西', 25), ('甘肃', 19), ('青海', 35), ('北京', 45), ('天津', 58), ('上海', 1), ('新疆', 15), ('宁夏', 26), ('西藏', 31), ('云南', 19), ('辽宁', 26), ('吉林', 34), ('山东', 12), ('广东', 43), ('广西', 15), ('贵州', 22), ('黑龙江', 28), ('内蒙古', 7), ('山东', 12), ('重庆', 20), ('四川', 42)]
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
c = (
    Map()
    .add("关注度",collect,"china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全国各地疫情关注情况填充图1",subtitle="关键词：武汉、疫情、战疫、钟南山、医院、口罩、肺炎\n（不含港澳台）"),
        visualmap_opts=opts.VisualMapOpts(max_=65,range_color=["oldlace","lightcoral","tomato","darkred"])
    )
    .render("全国各地疫情关注情况填充图1.html")
)

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
c = (
    Geo()
    .add_schema(maptype="china")
    .add( 
        "关注度",
        collect,
        type_=ChartType.HEATMAP,
        point_size = 30
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=65),
        title_opts=opts.TitleOpts(title="全国各地疫情关注情况热力图1",subtitle="关键词：武汉、疫情、战疫、钟南山、医院、口罩、肺炎\n（不含港澳台）"),
    )
    .render("全国各地疫情关注情况热力图1.html")
)





#第二组关键词Map地理位置图及热力图绘制代码
collect=[('河北', 16), ('山西', 13), ('江苏', 7), ('浙江', 18), ('安徽', 11), ('福建', 7), ('江西', 14), ('河南', 14), ('湖北', 15), ('湖南', 17), ('海南', 17), ('陕西', 18), ('甘肃', 26), ('青海', 21), ('北京', 21), ('天津', 17), ('上海', 0), ('新疆', 11), ('宁夏', 19), ('西藏', 11), ('云南', 13), ('辽宁', 20), ('吉林', 19), ('山东', 7), ('广东', 16), ('广西', 11), ('贵州', 11), ('黑龙江', 11), ('内蒙古', 13), ('山东', 7), ('重庆', 11), ('四川', 13)]
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
c = (
    Map()
    .add("关注度",collect,"china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全国各地疫情关注情况填充图2",subtitle="关键词：上班、办公室、复工、复产、工作 \n（不含港澳台）"),visualmap_opts=opts.VisualMapOpts(max_=26,range_color=["oldlace","lightcoral","tomato","darkred"])
    )
    .render("全国各地疫情关注情况填充图2.html")
)

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
c = (
    Geo()
    .add_schema(maptype="china")
    .add( 
        "关注度",
        collect,
        type_=ChartType.HEATMAP,
        point_size = 30

    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=26),
        title_opts=opts.TitleOpts(title="全国各地疫情关注情况热力图2",subtitle="关键词：上班、办公室、复工、复产、工作 \n（不含港澳台）"),
    )
    .render("全国各地疫情关注情况热力图2.html")
)




#第三组关键词Map地理位置图及热力图绘制代码
collect=[('河北', 10), ('山西', 2), ('江苏', 1), ('浙江', 2), ('安徽', 2), ('福建', 2), ('江西', 0), ('河南', 8), ('湖北', 4), ('湖南', 2), ('海南', 1), ('陕西', 2), ('甘肃', 0), ('青海', 2), ('北京', 3), ('天津', 2), ('上海', 0), ('新疆', 0), ('宁夏', 3), ('西藏', 0), ('云南', 2), ('辽宁', 3), ('吉林', 3), ('山东', 2), ('广东', 3), ('广西', 1), ('贵州', 2), ('黑龙江', 0), ('内蒙古', 1), ('山东', 2), ('重庆', 0), ('四川', 0)]
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
c = (
    Map()
    .add("关注度",collect,"china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全国各地疫情关注情况填充图3",subtitle="关键词：开学、返校、复学 \n（不含港澳台）"),visualmap_opts=opts.VisualMapOpts(max_=10,range_color=["oldlace","lightcoral","tomato","darkred"])
    )
    .render("全国各地疫情关注情况填充图3.html")
)

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
c = (
    Geo()
    .add_schema(maptype="china")
    .add( 
        "关注度",
        collect,
        type_=ChartType.HEATMAP,
        point_size = 30

    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=10),
        title_opts=opts.TitleOpts(title="全国各地疫情关注情况热力图3",subtitle="关键词：开学、返校、复学 \n（不含港澳台）"),
    )
    .render("全国各地疫情关注情况热力图3.html")
)






#疫情期间全国各地受关注度分布
collect=[('河北', 22.38019235186374),('山西', 14.799014079475809), ('江苏', 33.90236119974473), ('浙江', 47.09934281698226), ('安徽', 27.95968834267394), ('福建', 21.268505210783776), ('江西', 18.363633328325072), ('河南', 41.05438998839152), ('湖北', 89.377793056033), ('湖南', 45.24818630186573), ('海南', 29.93749634908581), ('陕西', 22.814333768397372), ('甘肃', 11.498620165580132), ('青海', 10.181521992087504), ('北京', 280.5540943363142), ('天津', 37.13183126234965), ('上海', 190.78508060669657), ('新疆', 33.52192265329438), ('宁夏', 10.629457124635216), ('西藏', 28.870880024708104), ('云南', 39.55641299671057), ('辽宁', 15.47454437450394), ('吉林', 6.992192052208368), ('山东', 54.34659541224156), ('广东', 75.851874902754), ('广西', 21.723712710288734), ('贵州', 17.88098416936868), ('黑龙江', 12.756338624662593), ('内蒙古', 17.779715065727594), ('重庆', 56.38733893840314), ('四川', 60.79078681853106)]
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType
c = (
    Map()
    .add("受关注度",collect,"china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="疫情期间全国各地受关注度分布",subtitle='（不含港澳台）'),
        visualmap_opts=opts.VisualMapOpts(max_=90,range_color=["oldlace","lightcoral","tomato","darkred"])
    )
    .render("疫情期间全国各地受关注度分布.html")
)




#疫情期间湖北各市受关注度分布
collect=[('武汉市', 227.12470148132067), ('黄石市', 4.554646650512853), ('十堰市', 1.6885046602728622), ('宜昌市', 3.4311791247062056), ('襄阳市', 2.6663467050620593), ('鄂州市', 1.8432755005645032), ('荆门市', 2.3577565474899322), ('孝感市', 4.0159208952826315), ('荆州市', 3.45239790612067), ('黄冈市', 8.983254157397182), ('咸宁市', 1.721570416533962), ('随州市', 1.2714935386936674), ('恩施土家族苗族自治州', 3.0708219274233177),('神农架林区', 1.7062225937995872), ('潜江市', 1.3086949693765377), ('天门市', 7.103137557332467), ('仙桃市', 1.7148173076510862), ('随州市', 1.2714935386936674)]
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType
c = (
    Map()
    .add("受关注度",collect,"湖北")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="疫情期间湖北各市受关注度分布"),
        visualmap_opts=opts.VisualMapOpts(max_=8,range_color=["oldlace","lightcoral","tomato","darkred"])
    )
    .render("疫情期间湖北各市受关注度分布.html")
)



#疫情期间全国各地积极度分布
collect=[('河北', 15), ('山西', 15), ('江苏', 16), ('浙江', 12), ('安徽', 15), ('福建', 5), ('江西', 16), ('河南', 12), ('湖北', 18), ('湖南', 15), ('海南', 15), ('陕西', 19), ('甘肃', 30), ('青海', 22), ('北京', 13), ('天津', 17), ('上海', 1), ('新疆', 14), ('宁夏', 10), ('西藏', 11), ('云南', 21), ('辽宁', 16), ('吉林', 10), ('山东', 12), ('广东', 12), ('广西', 12), ('贵州', 11), ('黑龙江', 14), ('内蒙古', 16), ('山东', 12), ('重庆', 18), ('四川', 44)]
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
c = (
    Map()
    .add("积极度",collect,"china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="疫情期间全国各地积极情绪分布",subtitle="关键词：积极、努力、赢、红火、恢复、胜、有望、一定、终于、认真、行动、加油、致敬、坚持、分享  \n(不含港澳台)"),visualmap_opts=opts.VisualMapOpts(max_=25,range_color=["oldlace","lightcoral","tomato","darkred"])
    )
    .render("疫情期间全国各地积极度分布.html")
)




#疫情期间全国各地消极度分布
collect=[('河北', 11), ('山西', 9), ('江苏', 10), ('浙江', 10), ('安徽', 11), ('福建', 8), ('江西', 8), ('河南', 11), ('湖北', 12), ('湖南', 14), ('海南', 8), ('陕西', 8), ('甘肃', 4), ('青海', 10), ('北京', 10), ('天津', 27), ('上海', 0), ('新疆', 4), ('宁夏', 5), ('西藏', 5), ('云南', 9), ('辽宁', 6), ('吉林', 11), ('山东', 12), ('广东', 14), ('广西', 12), ('贵州', 9), ('黑龙江', 9), ('内蒙古', 5), ('山东', 12), ('重庆', 10), ('四川', 13)]
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
c = (
    Map()
    .add("消极度",collect,"china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="疫情期间全国各地消极情绪分布",subtitle="关键词：发热、紧张、危、急、冲击、骚动、无望、不幸、不能、不要、不会、何时、熬夜、不吃  \n(不含港澳台)"),visualmap_opts=opts.VisualMapOpts(max_=15,range_color=["lightskyblue","skyblue","deepskyblue","steelblue","mediumblue","darkblue"])
    )
    .render("疫情期间各地消极度.html")
)




#疫情期间全国各地情绪分布总图
collect=[('河北', 4), ('山西', 6), ('江苏', 6), ('浙江', 2), ('安徽', 4), ('福建', -3), ('江西', 8), ('河南', 1), ('湖北', 6), ('湖南', 1), ('海南', 7), ('陕西', 11), ('甘肃', 26), ('青海', 12), ('北京', 3), ('天津', -10), ('上海', 1), ('新疆', 10), ('宁夏', 5), ('西藏', 6), ('云南', 12), ('辽宁', 10), ('吉林', -1), ('山东', 0), ('广东', -2), ('广西', 0), ('贵州', 2), ('黑龙江', 5), ('内蒙古', 11), ('山东', 0), ('重庆', 8), ('四川', 31)]
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
c = (
    Map()
    .add("情绪度",collect,"china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="疫情期间全国各地情绪分布",
                                  subtitle="积极关键词：积极、努力、赢、红火、恢复、胜、有望、一定、终于、认真、行动、加油、致敬、坚持、分享\n消极关键词：发热、紧张、危、急、冲击、骚动、无望、不幸、不能、不要、不会、何时、熬夜、不吃  \n(不含港澳台)"),
        visualmap_opts=opts.VisualMapOpts(max_=20,min_=-10,range_color=["mediumblue","steelblue","lightskyblue","oldlace","lightcoral","tomato","orangered","darkred"])
    )
    .render("疫情期间各地情绪分布.html")
)
