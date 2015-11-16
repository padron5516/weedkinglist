import urllib,urllib2,re,xbmcplugin,xbmcgui,requests


def CATEGORIES():
    addDir('This Is My Name','http://pastebin.com/raw.php?i=kQ6p9HtN',3,'')
def GET(url):
    r = requests.get(url)
    match = re.compile('<strong><a href="(.+?)">(.+?)<\/a><\/strong>').findall(r.content)
    for url,name in match:
        addDir(name,url,3,'')




def GET(''' ITEM TO BE USED'''):
    r = requests.get(''' THE ITEM THAT WAS USED''')
    match = re.compile('''REGEX''').findall(r.content)
    for ''' ITEMS''' in match:
        addDir(name,url,3,'')
        addDir('''NAME''','''URL''','''MODE''','''IMAGE''')








def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

                                ''' About this block of code'''
# This Block Adds A List Item One Then When Press Leads Or Links tTo Another

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
                                ''' About this block of code'''
# This Block Adds A List But Witch When Pressed Says In Same Directory But Carrys On The Code You Add To it

def addDir2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        
# Like The Above Block But With Added Infomation You Can Add Bellow Ads Fanart And Description        
                                ''' About this block of code'''
def addDir3(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        



              
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
   
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        OPEN_URL(url)
        
elif mode==2:
        print ""+url
        addSearch()
                                ''' END OF COPY CODE'''
###############################################################################################################
# OK Last it Remember The 3 now were are going to use it ok with this bellow code think of it as the url to your
# link and just like a link if its directed to the wrong place it will be wrong or spelled wrong il brake it down
# this is saying for the number 3
elif mode==3:
# Go To Def Name GET the brackts put any of the items that you wanted carried over 
    GET()
# it should look like bellow
elif mode==3:
    GET(url)
    ''' COPY BELOW CODE '''
xbmcplugin.endOfDirectory(int(sys.argv[1]))
################################################################################################################


                                            ''' END OF TUT'''


################################################################################################################



