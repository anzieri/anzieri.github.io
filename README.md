# Malicious URL Detector using Streamlit

Streamlit is a free, open-source Python framework that lets users create interactive web apps from data scripts. The training of the Machine Learning model used was done from scratch in the `MaliciousURLs(1).ipynb` notebook. The dataset used for the training was from Kaggle link https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset however feel free to use any other dataset available.

The model was trained using the Extreme Gradient Boosting (XGBoost) Classifier. Exportation of the model was done using pickle.

## Why This Project?

* **Enhanced Security:**  By scanning URLs before you click on them, a malicious URL detector can significantly reduce the risk of encountering phishing scams, malware, and other online threats. These threats can steal your personal information, damage your device, or even take control of your entire system.

* **Peace of Mind:** With a URL malicious detector, you can browse the web with more confidence, knowing that you're less likely to accidentally click on a dangerous link. This can be especially helpful if you frequently click on links in emails, social media posts, or from unknown sources.

* **Data Protection:**  Many malicious URLs are designed to steal sensitive data, such as your login credentials, credit card information, or social security number. A URL malicious detector can help to prevent this from happening by blocking access to these types of websites.

* **Improved Overall Cybersecurity:**  A URL malicious detector is just one piece of the cybersecurity puzzle, but it's an important one. By using a URL malicious detector in conjunction with other security measures, such as strong passwords and up-to-date software, you can significantly improve your overall online security posture.

* **Potential for Business Benefits:** In a business environment, URL malicious detectors can help to protect company data and resources from cyberattacks. They can also help to ensure that employees are not accidentally clicking on links that could compromise the security of the company network.

## WalkThrough

The URL is parsed and passed into various functions that is then extracted into 23 features to be used for the training and prediction process.
## Features 
1.	abnormal_url: simple url parsing
2.	sus_url: searches for a series of specific suspicious words(‘PayPal|login|signin|bank|account|update|free|lucky|service|bonus|ebayisapi|webscr’)
3.	digits: 
4.	count_question: number of question mark symbols
5.	count_non_alphanumeric 
6.	count_https: protocol search (https or http)
7.	count-www: appearance counts of www
8.	url_length: length of the entire string url
9.	hostname_length: string length of the hostname alone
10.	fd_length: string length of the first directory
11.	count-letters: number of letters
12.	short_url: shortened urls are accounted for (example: bit\.ly|goo\.gl|shorte\.st)
13.	count_embed_domian: number of double slashes
14.	use_of_ip: regex pattern search for ipv6 and ipv4
15.	count/ : number of slashes(directories)
16.	count% : number of percentage signs
17.	count= : number of equals 
18.	count- : number of hyphens
19.	count@ : number of at signs
20.	root_domain: country/organization based.(.com,.uk,.org)
21.	tld_length: string length of the top level domain
22.	file: file embedded within link (‘.bat|.dll|.pif|.exe|.scr|.application|.msp’)
23.	domain


![image](https://github.com/anzieri/anzieri.github.io/assets/88835282/f44b4ae0-46c9-4bcf-8e8c-43a5b7878ada)

