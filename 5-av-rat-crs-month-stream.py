import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

#read data and calculate maonth average rating
data = pandas.read_csv("reviews.csv",parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime("%Y-%m")
month_course_average = data.groupby(['Month','Course Name'])['Rating'].count().unstack()

chart_def = """
{

    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },


    title: {
        floating: true,
        align: 'left',
        text: 'Review Course Rating'
    },
    subtitle: {
        floating: true,
        align: 'left',
        y: 30,
        text: 'Average Course Rating by Month'
    },
    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [ ],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            }
        }
    },

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

}
"""
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp,text="Analyis of Course Reviews",classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp,text="These graphs represent course review analysis")

    hc = jp.HighCharts(a=wp,options=chart_def)
    hc.options.xAxis.categories = list(month_course_average.index)
    # basic structure auf the series data is a list out of dictonaries with name and data
    # template is [{'name': "name",'data': [value,value,.. ]}]
    # create that by inner for loops 
    hc_data = [{'name':v1,'data':[v2 for v2 in month_course_average[v1]]} for v1 in month_course_average.columns]
    hc.options.series = hc_data
    return wp

jp.justpy(app)
