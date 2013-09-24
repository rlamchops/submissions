# Andrew Zarenberg
# Period 6

from flask import Flask
import urllib2, StringIO, csv, operator



hTop = '''
<html>
<head>
<title>MetroCard Swipe Data</title>

<style type="text/css">
body {
font-family:Arial,Verdana;
padding-bottom:100px;
}

#header {
font-size:30px;
text-align:center;
margin-top:15px;
margin-bottom:10px;
}

#dateRange {
text-align:center;
font-size:20px;
font-style:italic;
margin-bottom:30px;
}

table.data {
border:2px solid black;
}

td, th.header {
padding:4px;
border:1px solid black;
}

th.header {
padding:8px;
font-weight:bold;
font-style:italic;
font-size:16px;
}

td.name {
font-weight:bold;
font-size:16px;
}

td.numTotal {
font-weight:bold;
}

span.perc {
font-style:italic;
font-size:13px;
}

td.numlist {
text-align:right;
}


#flag {
margin-top:50px;
text-align:center;
font-size:12px;
}


#nav {
border:2px solid black;
background:lightgray;
width:300px;
margin-bottom:10px;
padding:5px;
}
</style>

</head>
<body>'''

hBot = '''
</body>
</html>'''



# fm replaces removes white space then converts to int
def fm(n):
    a = n.replace(" ","")
    if a == "":
        return 0
    else:
        return int(a)



    


app = Flask(__name__)


@app.route("/")
def ind():
    return createTable("name")


@app.route("/sort/<n>")
def sortd(n):
    return createTable(n)



def createTable(n="name"):

    url = "http://www.mta.info/developers/data/nyct/fares/fares_130921.csv"

    dr = urllib2.urlopen(url).read()
    output = StringIO.StringIO(dr)
    cr = csv.reader(output)
    
    dateRange = ""

    for fin in cr:
        if fin[0].replace(" ","") == "":
            if fin[1].startswith("FARECARD"):
                True
            else:
                dateRange = fin[1]
                break





    col = 1
    rev = True
    
    rowHighlight = 0

    # sort
    if n == "fare_student":
        col = 24
        rowHighlight = 4
    elif n == "fare_full":
        col = 2
        rowHighlight = 2
    elif n == "fare_half":
        col = 3
        rowHighlight = 3
    elif n == "unlimited_week":
        col = 7
        rowHighlight = 5
    elif n == "unlimited_month":
        col = 8
        rowHighlight = 6
    else: # default sort by name
        rev = False

    n = sorted(csv.reader(output), key=operator.itemgetter(col), reverse=rev)




    data = []

    for row in n:
        data.append(row)


    page = hTop

    page += '''
<div id="header">Metrocard Swipe Data</div>
<div id="dateRange">'''+dateRange+'''</div>
<div id="nav">
   <strong>Order by:</strong>
   <div><a href="/sort/name">Station Name</a></div>
   <div><a href="/sort/fare_full"># Full Fare</a></div>
   <div><a href="/sort/fare_half"># Half Fare</a></div>
   <div><a href="/sort/fare_student"># Student Fare</a></div>
   <div><a href="/sort/unlimited_week"># Weekly Pass</a></div>
   <div><a href="/sort/unlimited_month"># Monthly Pass</a></div>
</div>
   

<table class="data" cellspacing="0">
   <tr>
      <th class="header">&nbsp;</th>
      <th class="header" id="head0">Station Name</th>
      <th class="header" id="head1">Total</th>
      <th class="header" id="head2">Full Fare</th>
      <th class="header" id="head3">Half Fare</th>
      <th class="header" id="head4">Student</th>
      <th class="header" id="head5">Weekly Pass</th>
      <th class="header" id="head6">Monthly Pass</th>
   </tr>'''

    if len(data) > 1:
        x=0
        while x < len(data):
            page += printStation(str(x),data[x])
            x += 1
    page += '''
</table>
<div id="flag">Data provided by the <a href="http://mta.info/developers/fare.html" target="_blank">MTA</a></div>'''


    page += hBot
    return page


def printStation(num,n):

    # remove headers from csv
    if n[0] == "REMOTE":
        return ""
    if n[0].replace(" ","") == "":
        return ""

    totalFare = 0
    x=2
    while x < len(n):
        totalFare += fm(n[x])
        x += 1





    r = '<tr><td class="numlist">'+num+'</td><td class="name">'+n[1]+'</td><td class="numTotal">'+str(totalFare)+'</td>'
    r += printNum(n[2],totalFare)    
    r += printNum(n[3],totalFare)
    r += printNum(n[24],totalFare)
    r += printNum(n[7],totalFare)
    r += printNum(n[8],totalFare)
    r += '</tr>'


#   <td class="num">'''+str(fm(n[2]))+'''</td>
#   <td class="num">'''+str(fm(n[24]))+'''</td>
#</tr>'''



    return r


def printNum(n,total):
    n = fm(n)
    if(total == 0):
        perc = 0
    else: perc = n*100/total
    return '<td class="num">'+str(n)+' <span class="perc">('+str(perc)+'%)</span></td>'


if __name__ == "__main__":
    app.run()
    
