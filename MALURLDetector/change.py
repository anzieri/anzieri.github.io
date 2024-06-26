# import module
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import dill as pickle
# from decompyle3 import Decompiler
# import sys

# from urllib.parse import urlparse
# import re
# from re import search as search
# Add title
st.title("Make things easier with MalDec! :mag:")

st.write("Welcome, this is a simple web app that helps you determine whether a URL is safe or not. Malicious urls are a major threat to internet users and with the power of a few ML Algorithms, its detection is now possible. The model was trained on a dataset of 1.2 million urls and exploits an XGBoost Classifier algorithm with a prediction accuracy of 96.7%")

url= st.text_input("Enter Url")
st.button('Predict')

path_name = '../anzieri.github.io/MALURLDetector/fifth_model.pkl'
# Create a decompiler object
# decompiler = Decompiler()

with open(path_name, 'rb') as file:
    data = pickle.load(file)
    xgb_c = data["model"]

    
    urlparse=data["urlparse"]
    
    tldextract=data["tldextract"]
    hashlib=data["hashlib"]
    abnormal_url = data["abnormal"]
    suspicious_words = data["sus_url"]
    count_https = data["https"]
    re=data["re"]
    os=data["os"]
    count_www = data["www"]
    url_length = data["url_length"]
    hostname_length = data["host_length"]
    count_percent = data["percent"]
    fd_length = data["fd_length"]
    count_questionmark = data["question"]
    count_forwardslash = data["forwardslash"]
    count_equals = data["equals"]
    count_hyphen = data["hyphen"]
    letter_count = data["letters"]
    digit_count = data["digits"]
    shortening_service = data["short_service"]
    no_of_embed = data["embedded"]
    having_ip_address = data["ip_address"]
    count_non_alphanumeric = data["non_alpha"]
    tld_length = data["tld"]
    extract_file_type = data["file"]
    extract_root_domain = data["root_domain"]
    extract_tld = data["tld"]
    count_attherate = data["rate"]
    main = data["main"]
    extract_rooty = data["rooty"]
    
    get_prediction_from_url = data["get_prediction"]
    
    result =get_prediction_from_url(url)

    if result =='SAFE': 
        st.success('The URL is ' + result + ' :four_leaf_clover: . Proceed with browsing.' )
    elif result =='DEFACEMENT':
        st.warning('The URL is most likely ' + result + '⚠️. Please proceed with browsing.')
    elif result =='PHISHING':
        st.warning('The URL is most likely ' + result + '⚠️. Please proceed with browsing.')
    elif result =='MALWARE':
        st.error('The URL is most likely ' + result + ' ⚠️. Please reconsider visiting this site.')
    else:
        st.error('Hmm, something went wrong. Please try again.')
    urlparse
    tldextract
    hashlib
    os
    re
    xgb_c
    suspicious_words(url)
    count_https(url)
    count_www(url)
    url_length(url)
    hostname_length(url)
    count_percent(url)
    fd_length(url)
    count_questionmark(url)
    count_forwardslash(url)
    count_equals(url)
    extract_rooty(url)
    count_hyphen(url)
    letter_count(url)
    digit_count(url)
    shortening_service(url)
    no_of_embed(url)
    having_ip_address(url)
    abnormal_url(url)
    count_non_alphanumeric(url)
    tld_length(url)
    extract_file_type(url)
    extract_root_domain(url)
    extract_tld(url)
    count_attherate(url)
    main(url)
