#-*- coding: utf-8 -*-
import mapnik
import csv

def render_tile():
    # создаем карту.
    m = mapnik.Map(1024, 786)
    # подключаем список цветов.
    colors = open('worldmap/static/colors.csv', 'r')
    colors_reader = csv.reader(colors)
    colors_lst = [row[2] for row in colors_reader]
    colors.close()
    m.background_color = mapnik.Color('lightyellow')

    for i in range(247):
        """Задаем параметры для каждого обьекта."""

        layer = mapnik.Layer('Build' + str(i))

        # запрос к бд по каждому обьекту.
        BUFFERED_TABLE = '(select * from worldmap_geoborder where id=%s) as id' % str(i + 1)
        datasource = mapnik.PostGIS(host='localhost', user='taga', password='nogiruki', dbname='gisdb',
                                    table=BUFFERED_TABLE, geometry_field='polygon_map')
        layer.datasource = datasource
        # стиль обьекта.
        style = mapnik.Style()

        # правила оформления для стиля.
        r = mapnik.Rule()

        polygon_symbolizer = mapnik.PolygonSymbolizer()
        polygon_symbolizer.fill = mapnik.Color(colors_lst[i])

        r.symbols.append(polygon_symbolizer)

        line_symbolizer = mapnik.LineSymbolizer()
        line_symbolizer.fill = mapnik.Color('black', 1)
        r.symbols.append(line_symbolizer)
        """
        text_symbolizer = mapnik.TextSymbolizer(Expression(['name']))

        text_symbolizer.fontset_name = "book-fonts"
        r.symbols.append(text_symbolizer)
        """
        style.rules.append(r)

        m.append_style('MyStyle' + str(i), style)
        layer.styles.append('MyStyle' + str(i))

        m.layers.append(layer)

    # выбираем область карты в соответсвии с параметрами из shapefile.
    extent = mapnik.Box2d(-180.000000, -90.000000, 180.000000, 83.623596)
    m.zoom_to_box(extent)

    # рендеринг изображения полученного из карты.
    mapnik.render_to_file(m, 'worldmap/static/tiles/0/0/0.png', 'png')