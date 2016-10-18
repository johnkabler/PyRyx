# PyRyx

## Python + Alteryx

PyRyx is a Python client helper for working with the Alteryx Gallery API.

It includes functions which allow a user to easily use Alteryx Applications as
data processing APIs, piping in data and retrieving the results.

## Usage
```python
from PyRyx import pyryx
```


```python
client_key = 'your_client_key_here'
client_secret = 'your_client_secret_here'
gallery_url = 'http://localhost:80/gallery/api/v1/'
```


```python
ayx = pyryx.PyRyxApi(client_key, client_secret, gallery_url)
```


```python
ayx.getSubscriptionWorkflows()
```




    [{'fileName': 'Tableau WDC Demo.yxwz',
      'id': '57acaca4065e3f26a82b2615',
      'isChained': False,
      'metaInfo': {'author': '',
       'copyright': '',
       'description': '#tableauwdc',
       'name': 'Tableau WDC Demo',
       'noOutputFilesMessage': '',
       'outputMessage': '',
       'url': '',
       'urlText': ''},
      'packageType': 0,
      'public': False,
      'runCount': 0,
      'runDisabled': False,
      'subscriptionId': '503bac188031af11f8f8e478',
      'uploadDate': '2016-08-11T16:49:40.732Z',
      'version': 1},
     {'fileName': 'Tableau WDC Demo 52.yxwz',
      'id': '57d71458065e3f31e07d96a0',
      'isChained': False,
      'metaInfo': {'author': '',
       'copyright': '',
       'description': '#tableauwdc',
       'name': 'Tableau WDC Demo 52',
       'noOutputFilesMessage': '',
       'outputMessage': '',
       'url': '',
       'urlText': ''},
      'packageType': 0,
      'public': False,
      'runCount': 0,
      'runDisabled': False,
      'subscriptionId': '503bac188031af11f8f8e478',
      'uploadDate': '2016-09-12T20:47:20.414Z',
      'version': 1}]




```python
ayx.getWorkflowQuestions('57acaca4065e3f26a82b2615')
```




    [{'description': 'Select Region',
      'items': [{'key': 'East', 'value': 'East'},
       {'key': 'West', 'value': 'West'}],
      'multiple': 'False',
      'name': 'Select Region',
      'type': 'QuestionListBox'},
     {'description': 'Orders on or after...',
      'name': 'Orders on or after',
      'type': 'QuestionDate'}]




```python
questions_list = ayx.getWorkflowQuestions('57acaca4065e3f26a82b2615')

questions = [{ "name": question['name']} for question in questions_list]

questions[0]['value'] = 'East'    

questions[1]['value'] = '2016-07-10'

question_param = { "questions" : questions }
```


```python
ayx.executeAndFetchResults('57acaca4065e3f26a82b2615', question_param)
```

    Running
    Completed





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Margin</th>
      <th>RecordID</th>
      <th>Region</th>
      <th>Sales</th>
      <th>State</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-10-17</td>
      <td>17804.6</td>
      <td>35</td>
      <td>East</td>
      <td>30197.6</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-08-25</td>
      <td>3067.71</td>
      <td>104</td>
      <td>East</td>
      <td>28119.2</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-10-02</td>
      <td>18371.8</td>
      <td>194</td>
      <td>East</td>
      <td>24885</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-10-17</td>
      <td>7107.53</td>
      <td>249</td>
      <td>East</td>
      <td>12340.5</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-10-08</td>
      <td>3599.09</td>
      <td>282</td>
      <td>East</td>
      <td>28586</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2016-09-22</td>
      <td>1063.48</td>
      <td>303</td>
      <td>East</td>
      <td>32159.7</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016-09-10</td>
      <td>11311.4</td>
      <td>365</td>
      <td>East</td>
      <td>17891.7</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2016-07-24</td>
      <td>7369.75</td>
      <td>413</td>
      <td>East</td>
      <td>24912.2</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016-09-22</td>
      <td>3942.1</td>
      <td>448</td>
      <td>East</td>
      <td>34925.2</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016-09-09</td>
      <td>9349.83</td>
      <td>456</td>
      <td>East</td>
      <td>15435.2</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016-09-28</td>
      <td>6813.12</td>
      <td>457</td>
      <td>East</td>
      <td>14590.9</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2016-07-23</td>
      <td>16332.3</td>
      <td>541</td>
      <td>East</td>
      <td>18840.4</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2016-07-11</td>
      <td>14735.8</td>
      <td>576</td>
      <td>East</td>
      <td>22774.7</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2016-08-04</td>
      <td>29911.7</td>
      <td>588</td>
      <td>East</td>
      <td>36416.6</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2016-08-31</td>
      <td>1895.27</td>
      <td>614</td>
      <td>East</td>
      <td>8063.33</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2016-08-30</td>
      <td>492.692</td>
      <td>628</td>
      <td>East</td>
      <td>2791.9</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2016-08-08</td>
      <td>9788.15</td>
      <td>695</td>
      <td>East</td>
      <td>48614.7</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2016-07-12</td>
      <td>27843.5</td>
      <td>736</td>
      <td>East</td>
      <td>29228.1</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2016-09-10</td>
      <td>10755.4</td>
      <td>755</td>
      <td>East</td>
      <td>15478.7</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2016-10-09</td>
      <td>12843.1</td>
      <td>774</td>
      <td>East</td>
      <td>23501.7</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2016-09-28</td>
      <td>2228.32</td>
      <td>780</td>
      <td>East</td>
      <td>36082.4</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2016-09-24</td>
      <td>9840.11</td>
      <td>789</td>
      <td>East</td>
      <td>18550.5</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2016-08-23</td>
      <td>3420.85</td>
      <td>1119</td>
      <td>East</td>
      <td>8035.69</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2016-09-21</td>
      <td>2383.95</td>
      <td>1135</td>
      <td>East</td>
      <td>10437.5</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2016-08-26</td>
      <td>7149.62</td>
      <td>1187</td>
      <td>East</td>
      <td>13409.9</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2016-08-25</td>
      <td>10939.4</td>
      <td>1279</td>
      <td>East</td>
      <td>18808.5</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2016-08-06</td>
      <td>13363.7</td>
      <td>1323</td>
      <td>East</td>
      <td>48917.8</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2016-10-15</td>
      <td>22499.8</td>
      <td>1359</td>
      <td>East</td>
      <td>37306.4</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2016-09-08</td>
      <td>4982.07</td>
      <td>1367</td>
      <td>East</td>
      <td>5659.37</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2016-10-15</td>
      <td>3073.99</td>
      <td>1375</td>
      <td>East</td>
      <td>6763.26</td>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1068</th>
      <td>2016-07-11</td>
      <td>24054.2</td>
      <td>714</td>
      <td>East</td>
      <td>49648.7</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1069</th>
      <td>2016-08-17</td>
      <td>9394.66</td>
      <td>725</td>
      <td>East</td>
      <td>40781.5</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1070</th>
      <td>2016-10-03</td>
      <td>19196.7</td>
      <td>739</td>
      <td>East</td>
      <td>43374.1</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1071</th>
      <td>2016-07-21</td>
      <td>2005.85</td>
      <td>759</td>
      <td>East</td>
      <td>31003.8</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1072</th>
      <td>2016-09-09</td>
      <td>5867.29</td>
      <td>767</td>
      <td>East</td>
      <td>8745.1</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1073</th>
      <td>2016-08-28</td>
      <td>14032.7</td>
      <td>793</td>
      <td>East</td>
      <td>46950.7</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1074</th>
      <td>2016-09-06</td>
      <td>18265.6</td>
      <td>819</td>
      <td>East</td>
      <td>28421.7</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1075</th>
      <td>2016-08-14</td>
      <td>4329.21</td>
      <td>865</td>
      <td>East</td>
      <td>34188.6</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1076</th>
      <td>2016-09-29</td>
      <td>4615.7</td>
      <td>913</td>
      <td>East</td>
      <td>17847.3</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1077</th>
      <td>2016-10-05</td>
      <td>432.833</td>
      <td>949</td>
      <td>East</td>
      <td>23058.7</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1078</th>
      <td>2016-09-26</td>
      <td>12082.3</td>
      <td>1022</td>
      <td>East</td>
      <td>19670</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1079</th>
      <td>2016-10-18</td>
      <td>5043.43</td>
      <td>1148</td>
      <td>East</td>
      <td>36855.9</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1080</th>
      <td>2016-08-27</td>
      <td>1007.93</td>
      <td>1195</td>
      <td>East</td>
      <td>8300.48</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1081</th>
      <td>2016-07-18</td>
      <td>40058.5</td>
      <td>1233</td>
      <td>East</td>
      <td>42945.8</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1082</th>
      <td>2016-09-22</td>
      <td>19342</td>
      <td>1297</td>
      <td>East</td>
      <td>43092.9</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1083</th>
      <td>2016-09-11</td>
      <td>34852.9</td>
      <td>1417</td>
      <td>East</td>
      <td>46387.8</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1084</th>
      <td>2016-07-27</td>
      <td>3039.1</td>
      <td>1426</td>
      <td>East</td>
      <td>3915.7</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1085</th>
      <td>2016-07-31</td>
      <td>-128.106</td>
      <td>1442</td>
      <td>East</td>
      <td>15710.8</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1086</th>
      <td>2016-09-08</td>
      <td>2075.26</td>
      <td>1571</td>
      <td>East</td>
      <td>49849.5</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1087</th>
      <td>2016-09-27</td>
      <td>22062.4</td>
      <td>1670</td>
      <td>East</td>
      <td>24968.3</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1088</th>
      <td>2016-07-30</td>
      <td>2126.33</td>
      <td>1684</td>
      <td>East</td>
      <td>29597.6</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1089</th>
      <td>2016-10-05</td>
      <td>33385.3</td>
      <td>1691</td>
      <td>East</td>
      <td>34251</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1090</th>
      <td>2016-09-17</td>
      <td>2038.66</td>
      <td>1779</td>
      <td>East</td>
      <td>2969.3</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1091</th>
      <td>2016-10-14</td>
      <td>2213.55</td>
      <td>1781</td>
      <td>East</td>
      <td>11631.7</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1092</th>
      <td>2016-07-26</td>
      <td>18308.7</td>
      <td>1795</td>
      <td>East</td>
      <td>30394.5</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1093</th>
      <td>2016-07-15</td>
      <td>5041.6</td>
      <td>1810</td>
      <td>East</td>
      <td>13318.9</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1094</th>
      <td>2016-09-30</td>
      <td>17063.2</td>
      <td>1882</td>
      <td>East</td>
      <td>35135.4</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1095</th>
      <td>2016-07-15</td>
      <td>1990.32</td>
      <td>1910</td>
      <td>East</td>
      <td>4927.32</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1096</th>
      <td>2016-09-27</td>
      <td>32378.4</td>
      <td>1947</td>
      <td>East</td>
      <td>42106.2</td>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>1097</th>
      <td>2016-08-02</td>
      <td>35421.7</td>
      <td>1965</td>
      <td>East</td>
      <td>49226.6</td>
      <td>Wisconsin</td>
    </tr>
  </tbody>
</table>
<p>1098 rows × 6 columns</p>
</div>




```python

```
