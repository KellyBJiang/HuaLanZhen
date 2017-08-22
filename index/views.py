# Some standard Django stuff
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader
from django.shortcuts import render
 
# list of mobile User Agents
mobile_uas = [
	'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
	'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
	'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
	'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
	'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
	'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
	'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
	'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
	'wapr','webc','winw','winw','xda','xda-'
	]
	
 
mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' ]
 
 
def mobileBrowser(request):
    ''' Super simple device detection, returns True for mobile devices '''
    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]
    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True
    return mobile_browser
 
 
def index(request):
    # if mobileBrowser(request):
    #     return render(request,'m_index.html')
    # else:
    #     return render(request,'index.html')
    return render(request,'index.html')   
def about(request):
    # if mobileBrowser(request):
    #     return render(request,'m_about.html')
    # else:
    #     return render(request,'about.html')
    return render(request,'about.html')
def art(request):
    # if mobileBrowser(request):
    #     return render(request,'m_about.html')
    # else:
    #     return render(request,'art.html')
    return render(request,'art.html')    
        
        
def contact(request):
    # if mobileBrowser(request):
    #     return render(request,'m_about.html')
    # else:
    #     return render(request,'contact.html') 
    return render(request,'contact.html')