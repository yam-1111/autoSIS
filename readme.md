
**update: ⚠️ this is unfinished work major bugs are expected.**


# autoSIS

simple python api for viewing grades and student portal for [PUP-SIS](https://sisstudents.pup.edu.ph/)

## ⚠️ disclaimer
The authors of this library are not responsible for any misusage, abuse, or illegal activities related to the usage of this library. It is crucial to exercise responsible and ethical behavior when utilizing this library.

This library is intended for educational purposes. following the established protocols and guidelines set forth by the institution. We strongly discourage any activities that violate these protocols or engage in any form of unauthorized access.

**Guidelines:**

- **Respect Protocols:** Please ensure that you respect the established protocols and guidelines when using this library to access the SIS. Abiding by these rules is crucial to maintaining the integrity and functionality of the system.

- **Avoid Flooding Requests:** Excessive and aggressive request patterns can negatively impact the SIS's performance, causing inconvenience to other users. Avoid flooding the system with an excessive number of requests, as this can lead to downtime and affect other iskolmates ability to access the SIS.

- **Ethical Use:** Use this library for legitimate and ethical purposes only. Engaging in any form of unauthorized access, data manipulation, or any other activities that violate the institution's policies is strictly prohibited.

## 🛠 Dependencies
* [playwright](https://playwright.dev/python/docs/intro)
* [selectolax](https://selectolax.readthedocs.io/)
* [pandas](https://pandas.pydata.org/)

## 🧰 Installation
* linux / ms-windows


```
pip install git+https://github.com/yam-1111/autoSIS
```

install the necessary tools for playwright to function properly
```
playwright install-deps 
playwright install firefox
```

## ⚙ Usage
### initialization
```
from autoSIS.utils import autoSIS
data = autoSIS(student_no="20xx-xxxxx-MN-0", student_birthday="1/01/1970," student_password="STUDENT_PASSWORD")
```
automatic screenshot can be disable by adding `isscreenshot=False` on the function parameters

### check if all grades are encoded in portal
```
# checks if the current sem has complete grades encoded
print(data.get_grades().is_complete())
```

### convert all data into pandas dataframe
```
df = data.get_grades().dataframe()
```





