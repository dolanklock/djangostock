from django.shortcuts import render, redirect
from . import models
import requests
from django.contrib import messages
from . import forms

API_KEY = "pk_b7a8c4f513b246919edb92e1558c4dbf"

def ticker_valid(ticker):
    """This does a webscrape for all ticker symbols in the nasdaq market and checks if
    users ticker symbol is a valid one

    Args:
        ticker (string): ticker symbol of stock

    Returns:
        bool: returns true if ticker symbol exists else false
    """
    from bs4 import BeautifulSoup
    TICKERS_NASDAQ = []
    response = requests.get("https://stockanalysis.com/list/nasdaq-stocks/")
    webpage_stock = response.text
    soup_test = BeautifulSoup(webpage_stock, "html.parser")
    all_anchor_tags = soup_test.find_all(class_="sym svelte-1tv1ofl")
    for tag in all_anchor_tags:
        tick = tag.a
        try:
            TICKERS_NASDAQ.append(tick.string)
        except Exception as ex:
            pass
    return ticker in TICKERS_NASDAQ

def main_render(request, TICKER=None):
    """this is the main render for api get requests

    Args:
        request (request): the HTTP request
        TICKER (string, optional): ticker symbol of stock. Defaults to None.

    Returns:
        render: _description_
    """
    import requests
    request_successful = True
    if TICKER is None:
        TICKER = "TSLA"
    try:
        response = requests.get(f"https://api.iex.cloud/v1/data/CORE/INTRADAY_PRICES/{TICKER}?token={API_KEY}")
        response_company_info = requests.get(f"https://api.iex.cloud/v1/data/core/company/{TICKER}?token={API_KEY}")
        json_data = response.json()
        json_data_company_info = response_company_info.json()
    except Exception as ex:
        request_successful = False
        return render(request, 'home.html', {"error": ex,
                                              "request_successful": request_successful})
    else:
        return render(request, 'home.html', {"json_data": json_data,
                                              "request_successful": request_successful,
                                              "company_name": json_data_company_info[0]['companyName'],
                                              "open": json_data[0]['open'],
                                              "close": json_data[0]['close'],
                                              "high": json_data[0]['high'],
                                              "low": json_data[0]['low'],
                                              "marketcap": json_data_company_info[0]['marketcap'],
                                              "sector": json_data_company_info[0]['sector'],
                                              "ceo": json_data_company_info[0]['ceo'],
                                              "longDescription": json_data_company_info[0]['longDescription'],
                                              })
    
def home(request):  # request coming from urls and calls this function and passes http request in to this function
    if request.method == "POST":
        TICKER = request.POST['ticker']
        if ticker_valid(TICKER):
            return main_render(request=request, TICKER=TICKER)
        else:
            return render(request, 'home.html', {"error": "Ticker symbol does not exist"})
    else:
        return render(request, 'home.html', {"no_symbol": "Enter a Ticker Symbol..."})

def add_stock(request):
    if request.method == "POST":
        form = forms.StockForm(request.POST or None)
        if form.is_valid():  # checks if valid
            form.save()  # saves to database
            messages.success(request,
                            ('stock has been added successfully'))  # this message gets listed on the admin page inside the new database
            return redirect('addstock')  # this should be the html 'addstock' - redirects it to that html
    # else:  #TODO: fix this, want code in here to always show. 
    ticker = models.Stock.objects.all()  # this gets the objects of class Stock from models
    return render(request, "addstock.html", {'ticker': ticker})

def delete_stock(request, stock_id):
    item = models.Stock.objects.get(pk=stock_id)  # pk is primary key. getting all objects in database 'stock'. and then getting the specific item that matches id passed in
    item.delete()  # deletes the item from database
    messages.success(request, ("Ticker symbol deleted"))  # this message gets listed on the admin page inside the new database
    return redirect("addstock")  # redirects page back to addstock html file

def about(request):
    return render(request, 'about.html', {})
