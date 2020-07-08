from django.shortcuts import render, HttpResponse
from bokeh.io import output_file, show
from bokeh.embed import components
from bokeh.plotting import figure
# Create your views here.


def visual_1(request):
  # lazımi modulların yüklənməsi, bokeh.io bizə faylın ixracı və görüntüsü, figure funksiyası isə vizuallaşdırmanın yerini hazırlayır.
  # xəyali məlumat setimizi yaradaq

  x = [5, 6, 7, 8, 9, 10]
  y = [1, 2, 3, 4, 5, 6]

  # figure() funksiyasını istifadə edirik, dediyim kimi çərçivə yaratmağa
  plot = figure(plot_width=400, plot_height=400, title='Zen of Analytics', x_axis_label= 'X Axis', y_axis_label= 'Y Axis')

  #  line() xəttimizi yaradırıq
  plot.line(x, y, line_width=5, legend_label='ZenLife', line_color='green')

  # xətt ilə məlumatın nöqtələrinin kəsişməsində göstəricilər yarada bilərik, burada dairə (circle) də ola bilərdi
  plot.cross(x, y, size=15, color='navy')

  # nəticəni çağırırıq

  script, div = components(plot)
  return render(request, 'visual_1.html', {"script": script, 'div': div})
