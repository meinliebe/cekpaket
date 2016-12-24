from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.


def index(request):
	return render(request, 'base.html')

def get_paket(request):
	pengirim = ''
	resi = ''
	if request.method == 'POST':
		resi = request.POST.get('input_resi')
		pengirim = request.POST.get('input_pengirim')
	
	url = 'http://ibacor.com/api/cek-resi'
	keys = '7b5c7b3dce3a4719738a644b99315d4c'
	params = {'pengirim': pengirim, 'resi': resi, 'k': keys}

	r = requests.get(url, params=params)
	ret = r.json()
	
	if ret['status'] == 'success' and ret['pesan'] == 'data ada':
		ret_list = {'data': ret['data'], 'query': ret['query'], 'website': ret['website']}
		return render(request, 'result.html', ret_list)
	return render(request, '404.html')		
	