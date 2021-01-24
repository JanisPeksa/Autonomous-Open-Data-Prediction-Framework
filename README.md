<p>AUTONOMOUS OPEN DATA PREDICTION FRAMEWORK</p>
<p>&nbsp;</p>
<p>Documentation</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>Riga Technical University<br/>Faculty of Computer Science and Information Technology</p>
<p>Information Technology Institute<br/>Department of Management Information Technology</p>
<p><strong>Jānis Pek&scaron;a </strong>Research Assistant <br/><a href="http://iti.rtu.lv/vitk/lv/katedra/darbinieki/janis-peksa">http://iti.rtu.lv/vitk/lv/katedra/darbinieki/janis-peksa</a></p>
<p>&nbsp;</p>
<p><strong>INDEX</strong></p>
<p>&nbsp;</p>
<p><a href="#_Toc57222855">1..... INTRODUCTION.. 3</a></p>
<p><a href="#_Toc57222856">2..... WEBSITE CONNECTION.. 4</a></p>
<p><a href="#_Toc57222857">3..... MYSQL CONNECTION.. 6</a></p>
<ol start="4">
<li><a href="#_Toc57222858"> MongoDB CONNECTION.. 8</a></li>
<li><a href="#_Toc57222859"> Difference between database clients. 8</a></li>
<li><a href="#_Toc57222860"> MongoDB Importing. 8</a></li>
</ol>
<p><a href="#_Toc57222861">III.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; MongoDB Exporting. 10</a></p>
<ol start="5">
<li><a href="#_Toc57222862"> DATA HANDLING.. 11</a></li>
<li><a href="#_Toc57222863"> For exporting to MongoDB.. 11</a></li>
<li><a href="#_Toc57222864"> Process data from MongoDB.. 12</a></li>
</ol>
<p><a href="#_Toc57222865">III.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Process data from MySQL. 15</a></p>
<ol>
<li><a href="#_Toc57222866"> Accuracy. 18</a></li>
</ol>
<p><a href="#_Toc57222867">6..... ESTIMATION.. 20</a></p>
<p><a href="#_Toc57222868">7..... PLOTS. 22</a></p>
<p><a href="#_Toc57222869">9..... Kalman Filter 1D and 2D.. 29</a></p>
<p><a href="#_Toc57222870">10....... API 31</a></p>
<ol>
<li><a href="#_Toc57222871"> /get/estimates/all 31</a></li>
<li><a href="#_Toc57222872"> /get/estimates 32</a></li>
</ol>
<p><a href="#_Toc57222873">III.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /get/accuracies. 32</a></p>
<ol>
<li><a href="#_Toc57222874"> /use/1d_kalman_filter 32</a></li>
<li><a href="#_Toc57222875"> /use/2d_kalman_filter 32</a></li>
<li><a href="#_Toc57222876"> /get/forecast/arima. 33</a></li>
</ol>
<p><a href="#_Toc57222877">VII.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /get/forecast/arima/time_period. 33</a></p>
<p><a href="#_Toc57222878">VIII.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /get/forecast/ar 34</a></p>
<ol>
<li><a href="#_Toc57222879"> /get/forecast/ma. 34</a></li>
<li><a href="#_Toc57222880"> /get/forecast/arma. 34</a></li>
<li><a href="#_Toc57222881"> /get/forecast/all_models. 34</a></li>
</ol>
<p><a href="#_Toc57222882">XII.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /get/forecast/all_models/with/1d_kalman_filter 35</a></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><br /> </p>
<h1><a name="_Toc57222438"></a><a name="_Toc57222855"></a>1.&nbsp;&nbsp;&nbsp;&nbsp; INTRODUCTION</h1>
<p>This is the detailed documentation of the program, which is part of the Autonomous Open Data Prediction Framework (AODPF). Here are described methods to implement all essential functionality. Some of the methods aren&rsquo;t described because they are built-in in Python or taken from Python modules. It will be announced if some of Python files described below use other modules for Python. All these functions, methods, and modules written not by me have their references, description, and examples of usage on the Internet. All of them can be used freely, as provided and without almost any limitations.</p>
<p>Special thanks to outstanding supervisor Prof. Janis Grabis</p>
<p>This research was supported by Riga Technical University's Doctoral Grant programme.</p>
<p><br /> </p>
<p>&nbsp;</p>
<h1><a name="_Toc57222439"></a><a name="_Toc57222856"></a>2.&nbsp;&nbsp;&nbsp;&nbsp; WEBSITE CONNECTION</h1>
<p>The first source of data is the website <a href="http://www.lvceli.lv/cms">www.lvceli.lv/cms. </a>The <strong>Request.py </strong>to implement the needed functionality. At the core of it are such modules as <strong>requests </strong>and <strong>BeautifoulSoup. </strong>First, one is needed to make GET/POST requests to the website, and the second one is needed to process HTML properly, which is returned by requests.o</p>
<p>Examples of using and explanation:</p>
<p>&nbsp;</p>
<p>table = Request.get_table()&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>Firstly, to get a table from the website. This method does everything it needs to return the correct table with observations that it contains. No need to pass the URL of the website because it's given as a default parameter, as shown in the definition below. Now to have a table with data, but before need to separate HTML values because this method only returns part of the webpage.</p>
<p>data_lists = Request.get_data_lists_from_table(table)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
<p>&nbsp;</p>
<p>Now using another method that will extract all data from HTML, save it to lists and return a list of records like [[], [], []].</p>
<p>This data program can process correctly, export to the database, and make estimations, but before this operations, some more functionality will be described to understand what is going on inside altogether.</p>
<p>Because working with databases to store vast amounts of data, this module is crucial for gathering data in real-time and has some simple methods to work. Still, it is much more convenient to import/export data using clients of databases described next.</p>
<p><em>Definitions:</em></p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_table(url='<a href="http://www.lvceli.lv/cms/%27)">http://www.lvceli.lv/cms/'):</a></p>
<p><em>with </em>requests.session() <em>as </em>s:</p>
<p>r = s.post(url, data=login_data, headers=headers)</p>
<p><em>&nbsp;</em></p>
<p>soup = BeautifulSoup(r.content, 'html5lib')</p>
<p><em>return </em>soup.find("table", attrs={"class": "norm", "id": "table-1"})</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_table() </em></p>
<p><em>&nbsp;</em></p>
<p>This method makes a POST request to a website with data that contains login and password to get access to the table with observations. Because every successful application returns a whole webpage to separate our table from the whole piece of HTML to get by using unique attributes of the table that are needed. In details:</p>
<p>soup &ndash; an instance of <strong>class BeautifulSoup</strong>, where HTML will be stored.</p>
<p>Using method <em>find(), </em>and in arguments, passing the tag that looks for, and it is unique attributes to be sure that a correct table in the result is taken.</p>
<p>&nbsp;</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_data_lists_from_table(table) -&gt; <em>list</em>: tmp_list = []</p>
<p>data_list = []</p>
<p><em>&nbsp;</em></p>
<p><em>for </em>row <em>in </em>table.find_all('tr'):</p>
<p><em>for </em>cell <em>in </em>row.find_all('td'): tmp_list.append(cell.text)</p>
<p><em>&nbsp;</em></p>
<p><em>while </em><em>len</em>(tmp_list) &lt; 19: tmp_list.append('-')</p>
<p><em>&nbsp;</em></p>
<p>data_list.append(tmp_list) tmp_list = []</p>
<p><em>&nbsp;</em></p>
<p>data_list.pop(0)</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>data_list</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_data_lists_from_table() </em></p>
<p><em>&nbsp;</em></p>
<p>This method is iterating through every row in the table and through every cell of row (loop in loop, internal circuit) and taking text from HTML tags and adding it to the temporal list, which appends to the main index of data. At the end of the method, the first list of data is being deleted because it contains only titles of columns that are not needed in our main list.</p>
<p>&nbsp;</p>
<h1><a name="_Toc57222440"></a><a name="_Toc57222857"></a>3.&nbsp;&nbsp;&nbsp;&nbsp; MYSQL CONNECTION</h1>
<p>To get data from the MySQL database, MySQLClient.py, which has few methods to download data from a table in the database, uses <strong>mysql.connector </strong>module for Python to get a possibility to connect to the database.</p>
<p>A simple instruction to start:</p>
<ol>
<li>Firstly, it is needed to create a client:</li>
</ol>
<table width="100%">
<tbody>
<tr>
<td>
<p>sql_client = MySQLClient('xx.xx.xx.xx', 'xxx', 'xxx', 'xxx')</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>In parameters, we pass the IP address of the database, login, and password to get access and the table's name to get data from. In this case, it is a database with observations for one month.</p>
<ol start="2">
<li>Now it is connected to the database and have two ways: get all of the data stored in the database or data from exact station/s. It can be either use <em>get_all_info_from_database</em>() or <em>get_info_by_station()/get_info_by_stations(). </em>The difference is in the amount of returned data&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; and&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; which&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data is&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Example:</li>
</ol>
<table width="100%">
<tbody>
<tr>
<td>
<p>records = sql_client.get_info_by_station('LV01')</p>
</td>
</tr>
</tbody>
</table>
<p>Now in variable <em>records </em>is stored all of the observations from the station with code "LV01".</p>
<table width="100%">
<tbody>
<tr>
<td>
<p>records = sql_client.get_all_info_from_database()</p>
</td>
</tr>
</tbody>
</table>
<p>But using the method to get all of the stored observations, it will get all of them and store in</p>
<p>variable <em>records.</em></p>
<table width="100%">
<tbody>
<tr>
<td>
<p>records = sql_client.get_info_by_stations(['LV01', 'LV02', 'LV03'])</p>
</td>
</tr>
</tbody>
</table>
<p>By using this method, it can pass a list of station codes and return lists of data for every</p>
<p>a station that is asked.</p>
<p><em>Definitions</em></p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em><em>init</em> (<em>self</em>, host, username, password, database):</p>
<p><em>self</em>.host = host <em>self</em>.username = username <em>self</em>.password = password <em>self</em>.database = database</p>
<p><em>self</em>.database_connection = <em>self</em>.connect_to_database() <em>self</em>.cursor = <em>self</em>.database_connection.cursor()</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of MySQLClient init () also known as class constructor </em></p>
<p>Here is just create an instance of the class with all the needed variables. <em>self.cursor </em>is a variable</p>
<p>responsible for interaction with the database: making queries, executing commands, and returning results.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>connect_to_database(<em>self</em>):</p>
<p>database_connection = mysql.connector.connect( host=<em>self</em>.host,</p>
<p>user=<em>self</em>.username, passwd=<em>self</em>.password, database=<em>self</em>.database</p>
<p>)</p>
<p><em>return </em>database_connection</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of MySQLClient connect_to_database() </em></p>
<p>&nbsp;</p>
<p>This method establishes the connection to the database using data provided to <em>init () </em>and method of <strong>mysql.connector </strong>and returning it to variable in <em>init ().</em></p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_all_info_from_database(<em>self</em>): command = 'SELECT * FROM data_records' <em>self</em>.cursor.execute(command)</p>
<p>records = <em>self</em>.cursor.fetchall() <em>return </em>records</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_all_info_from_database() </em></p>
<p>In this method, a simple executing query written and stored in variable <em>command </em>and</p>
<p>returning all observations from the database.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_info_by_station(<em>self</em>, station_code: <em>str </em>= 'LV01'):</p>
<p>command = 'SELECT * FROM data_records WHERE stacijas_kods = %s'</p>
<p><em>self</em>.cursor.execute(command, (station_code,)) records = <em>self</em>.cursor.fetchall()</p>
<p><em>return </em>records</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_info_by_station() </em></p>
<p>In this method, executing the query to the database and returning all rows in the database</p>
<p>with data from the station passed in parameters or defined as the default parameter. In variable</p>
<p><em>command, the </em>SQL command is constructed to make a proper query.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_info_by_stations(<em>self</em>, station_codes: <em>list</em>) -&gt; <em>list</em>: info = []</p>
<p><em>for </em>station_code <em>in </em>station_codes:</p>
<p>command = 'SELECT * FROM data_records WHERE stacijas_kods = %s'</p>
<p><em>self</em>.cursor.execute(command, (station_code,)) records = <em>self</em>.cursor.fetchall() info.append(records)</p>
<p><em>else</em>:</p>
<p><em>return </em>info</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_info_by_stations() </em></p>
<p>This method does almost everything the same as the previous one; however, for many stations</p>
<p>and returns a list of records from many stations.</p>
<p>&nbsp;</p>
<h1><a name="_Toc57222441"></a><a name="_Toc57222858"></a>4. MongoDB CONNECTION</h1>
<p>&nbsp;</p>
<h2><a name="_Toc57222442"></a><a name="_Toc57222859"></a>I.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Difference between database clients</h2>
<p><em>&nbsp;</em></p>
<p>Compared with the MySQL module, the program has methods for importing and exporting data if a user with a login/password passed to <em>MongoDBClient </em>has permission to do so.</p>
<p>This program is capable of working with MongoDB as well. Methods are located in <strong>MongoDBClient.py </strong>and <strong>AutoDBFiller.py</strong><em>. </em>They use the<strong> pymongo </strong>module to connect to the MongoDB cluster, where databases with data collections are stored.</p>
<p>A simple instruction to start:</p>
<ol>
<li>In the case with MySQL, first of all, is creating a client that will connect to the cluster:</li>
</ol>
<table width="100%">
<tbody>
<tr>
<td>
<p>mongo_db_client = MongoDBClient('login', 'password', 'MeteoInfoTable', 'LastInsertTable')</p>
</td>
</tr>
</tbody>
</table>
<p>In arguments, passing login and password through connecting to the cluster, name of the database</p>
<p>where observations are stored and the name of the database where the last insert is stored.</p>
<p><em>Definitions</em></p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em><em>init </em>(<em>self</em>, login: <em>str</em>, password: <em>str</em>, main_database_name: <em>str</em>, time_database_name: <em>str</em>):</p>
<p><em>self</em>.my_client = <em>self</em>.get_connection(login, password)</p>
<p><em>self</em>.main_database_name = main_database_name</p>
<p><em>self</em>. main_database = <em>self</em>.my_client[<em>self</em>.main_database_name] <em>self</em>.time_database_name = time_database_name</p>
<p><em>self</em>. time_database = <em>self</em>.my_client[<em>self</em>.time_database_name] <em>self</em>.is_it_first_filling = <em>self</em>.is_not_first_filling_made()</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of MongoDBClient init () also known as the class constructor </em></p>
<p>In this method, creating our client by establishing a connection and defining essential variables.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_connection(login, password):</p>
<p><em>return </em>pymongo.MongoClient( "mongodb+srv://xxxxx".format(login, password))</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_connection() </em></p>
<p>In this method, an establishing connection using login and password provided to <em>init () </em>and</p>
<p>returning it to the class constructor.</p>
<p>&nbsp;</p>
<h2><a name="_Toc57222443"></a><a name="_Toc57222860"></a>II.&nbsp; MongoDB Importing</h2>
<p><em>&nbsp;</em></p>
<ol>
<li>records =&nbsp;&nbsp;&nbsp; mongo_db_client.get_all_info_from_main_database() Now it is stored all information from main database in list of lists with dictionaries inside. Consider this as two-dimension array of dictionaries like [[{}, {}, {}], [{}, {},</li>
</ol>
<p>{}]]</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<ol start="2">
<li>records = mongo_db_client.get_data_from_collection('A1 km 12 Ādaži') If needed to get info from one station, it is possible to use this method and pass the name of the</li>
</ol>
<p>&nbsp;</p>
<p>&nbsp;</p>
<table width="100%">
<tbody>
<tr>
<td>
<p>3. records = mongo_db_client.get_data_from_collections(['A1 km 12</p>
<p>Ādaži', 'A1 km 21 Lilaste'])</p>
</td>
</tr>
</tbody>
</table>
<p>In case needed observations from many stations, it is possible to use this method and</p>
<p>pass list of station names.</p>
<ol start="4">
<li>Please, be attentive that in the MySQL database, station codes were used but with MongoDB names of stations!</li>
<li>How to process this data correctly and use it in estimations is described</li>
</ol>
<p><em>Definitions</em></p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_all_info_from_main_database(<em>self</em>) -&gt; <em>list</em>:</p>
<p>collection_names = <em>self</em>. main_database.list_collection_names() list_of_info = []</p>
<p>temp_list = []</p>
<p><em>for </em>name <em>in </em>collection_names:</p>
<p><em>for </em>search_result <em>in </em><em>self</em>. main_database[name].find(): search_result.pop('_id')</p>
<p>search_result['Station'] = name temp_list.append(search_result)</p>
<p>list_of_info.append(temp_list) temp_list = []</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>list_of_info</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_all_info_from_main_database() </em></p>
<p>In this method, calling for all collections present in the central database, and depending on names</p>
<p>returned in the list, requests are being made in the loop. In <em>for </em>loop, we are deleting <em>id </em>keyword with the value from every returned result because it is unnecessary and adding the <em>Station </em>keyword with a value of the name of the collection getting at this moment, so every result has the name of the station it relates. As a result, getting a list of lists of dictionaries as it was described earlier.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_data_from_collection(<em>self</em>, station_name: <em>str</em>) -&gt; <em>list</em>: list_of_info = []</p>
<p><em>for </em>search_result <em>in </em><em>self</em>. main_database[station_name].find(): search_result.pop('_id')</p>
<p>search_result['Station'] = station_name list_of_info.append(search_result)</p>
<p><em>else</em>:</p>
<p><em>return </em>list_of_info</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_data_from_collection() </em></p>
<p>In this method, passing the name of one station as a parameter and making a request to the database, processing results of search the same as in the previous method and returning list of info.</p>
<p>&nbsp;</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_data_from_collections(<em>self</em>, station_names: <em>list</em>) -&gt; <em>list</em>: list_of_info = []</p>
<p><em>&nbsp;</em></p>
<p><em>for </em>station_name <em>in </em>station_names:</p>
<p><em>for </em>search_result <em>in </em><em>self</em>. main_database[station_name].find(): search_result.pop('_id')</p>
<p>search_result['Station'] = station_name list_of_info.append(search_result)</p>
<p><em>else</em>:</p>
<p><em>return </em>list_of_info</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_data_from_collections() </em></p>
<p>In this method, passing the list of station names, but the logic is the same as in the two previous methods. The only difference is that it iterates through the given list of names containing the user-provided names.</p>
<p>&nbsp;</p>
<h2><a name="_Toc57222444"></a><a name="_Toc57222861"></a>III.&nbsp;&nbsp;&nbsp;&nbsp; MongoDB Exporting</h2>
<p><em>&nbsp;</em></p>
<ol>
<li>To use all of the functionality, it should recreate the client and use AutoDBFiller()</li>
</ol>
<table width="100%">
<tbody>
<tr>
<td>
<p>mongo_db_client = AutoDBFiller('login', 'password', 'MeteoInfoTable', 'LastInsertTable')</p>
</td>
</tr>
</tbody>
</table>
<p>Parameters are the same as in the case with MongoDBClient() because <strong><em>class AutoDBFiller </em></strong>is a child-class of <strong><em>class MongoDBClient </em></strong>and has all of its methods and some new.</p>
<ol start="2">
<li>As described earlier, it is possible to use requests to take data from the website, but this data must be processed before it can be exported to the database, so be sure to check the Data Handling chapter and methods presented</li>
</ol>
<p>&nbsp;</p>
<h1><a name="_Toc57222445"></a><a name="_Toc57222862"></a>5. DATA HANDLING</h1>
<p>Created <strong>DataHandler.py </strong>with methods to process data in different ways to prepare it for different usage. This chapter will be separated into many small to systemize data and increase the readability of the document.</p>
<p>&nbsp;</p>
<h2><a name="_Toc57222446"></a><a name="_Toc57222863"></a>I.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For exporting to MongoDB</h2>
<p><em>&nbsp;</em></p>
<p>After getting the list of lists of values from the website, it needs to turn it into a JSON-like document to export it to MongoDB because this database contains all records in JSON. Python is a data type called the <em>dictionary, </em>so a set of methods will help prepare all the data to export.</p>
<p>data_dicts = DataHandler.get_data_dicts(data_lists)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Here using variable <em>data_lists </em>from the Website Connection chapter, which contains a list of lists of values from the website. After calling this method, turning a list of lists into a list of dictionaries like [{}, {}, {}]</p>
<p>Now data can be exported to the database. This process will be described in the MongoDB Exporting chapter.</p>
<p><em>Definitions</em></p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_data_dicts(data_lists) -&gt; <em>list</em>: data_dicts = []</p>
<p><em>&nbsp;</em></p>
<p><em>for </em>data <em>in </em>data_lists:</p>
<p>data_dict = {'Station': data[0],</p>
<p>'Time': data[1],</p>
<p>'Date': DataHandler.get_date(), 'Air Temperature': data[2],</p>
<p>'Air Temperature(-1 h)': data[3], 'Humidity': data[4],</p>
<p>'Dew Point': data[5], 'Precipitation': data[6], 'Intensity': data[7], 'Visibility':&nbsp; data[8], 'Road Temperature': data[9],</p>
<p>'Road Temperature(-1 h)': data[10], 'Road Condition': data[11],</p>
<p>'Road Warning': data[12], 'Freezing Point': data[13], 'Road Temperature 2': data[14],</p>
<p>'Road Temperature 2(-1 h)': data[15], 'Road Condition 2': data[16],</p>
<p>'Road Warning 2': data[17], 'Freezing Point 2': data[18]}</p>
<p>data_dicts.append(data_dict)</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>data_dicts</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_data_dicts() </em></p>
<p>This method iterates through a list of data, takes values from the list by indexes they are stored,</p>
<p>Furthermore, append the created dictionary to the list, which will be returned in the result.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_date() -&gt; <em>str</em>:</p>
<p><em>from </em>datetime <em>import </em>datetime</p>
<p><em>&nbsp;</em></p>
<p>year = datetime.now().year</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_date() </em></p>
<p>&nbsp;</p>
<table width="100%">
<tbody>
<tr>
<td>
<p>month = datetime.now().month day = datetime.now().day</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>'Year: {} Month: {} Day: {}'.format(year, month, day)</p>
</td>
</tr>
</tbody>
</table>
<p>This method takes the current date-time, adds its parts to the string (year, month, and day), and returns this string. It uses the <strong>DateTime </strong>module to obtain the current date and time.</p>
<p>&nbsp;</p>
<h2><a name="_Toc57222447"></a><a name="_Toc57222864"></a>II.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Process data from MongoDB</h2>
<p><em>&nbsp;</em></p>
<table width="100%">
<tbody>
<tr>
<td>
<p>lists_of_measurements, list_of_station_names = DataHandler.get_prepared_lists_for_estimation(main_data, 'Dew Point')</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Data from MongoDB database</em></p>
<p>The called method returns two lists: with measurements (observations) and with station names</p>
<p>whose data returned. Because of the chance that sometimes stations have not been gathering data program checks every list and, if it is possible to fill missing data, it fills, if not &ndash; deletes the list of data. Station names are not needed for estimation but are essential for building plots. Plots are described later.</p>
<p><em>Definitions</em></p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_prepared_lists_for_estimation(main_data, value: <em>str </em>= 'Dew Point') -&gt; <em>tuple</em>: lists_of_chosen_values = DataHandler.get_lists_of_chosen_values_with_station_names(main_data, value)</p>
<p><em>&nbsp;</em></p>
<p>lists_of_measurements_with_station_names = DataHandler.get_lists_of_measurements_with_station_names( lists_of_chosen_values)</p>
<p>list_of_station_names = DataHandler.get_station_names(lists_of_measurements_with_station_names) lists_of_measurements_without_station_names = DataHandler.get_lists_of_measurements_without_station_names(</p>
<p>lists_of_measurements_with_station_names)</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>lists_of_measurements_without_station_names, list_of_station_names</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_prepared_lists_for_estimation() </em></p>
<p>This method does a lot, but basically, it does what it has to. Here are four steps:</p>
<ol>
<li>Getting a list of lists of chosen values or values defined as a default parameter, and at the end of every list, appending the name of the station to which it is related. For this goal is used <em>get_lists_of_chosen_values_with_station_names().</em></li>
<li>Because all values are stored as text(string type), to convert it to numbers to be able to work with data, for this goal is used <em>get_lists_of_measurements_with_station_names() </em>In this method are being checked lists of data is it possible to fill missing data and if it is possible, it is being As a result, eligible lists returned. Those who were not fillable were deleted.</li>
<li>The program starts dividing the list of data into two lists: list of station names and list_of_measurements. For first goal is used <em>get_station_names().</em></li>
<li><em>For </em>last step is used <em>get_list_of_measurements_without_station_names().</em></li>
</ol>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_lists_of_chosen_values_with_station_names(lists_of_dicts: <em>list</em>, value_name: <em>str</em>) -&gt;</p>
<p><em>list</em>:</p>
<p>list_of_values = [] temp_list = []</p>
<p><em>&nbsp;</em></p>
<p><em>for </em>list_of_dicts <em>in </em>lists_of_dicts:</p>
<p><em>for </em>data_dict <em>in </em>list_of_dicts: temp_list.append(data_dict[value_name])</p>
<p><em>else</em>:</p>
<p>temp_list.append(data_dict['Station']) list_of_values.append(temp_list)</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_lists_of_chosen_values_with_station_names() </em></p>
<p>&nbsp;</p>
<table width="100%">
<tbody>
<tr>
<td>
<p>temp_list = []</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>list_of_values</p>
</td>
</tr>
</tbody>
</table>
<p>Here is a simple method that fills the list with lists of values passed as an argument and station name values.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_lists_of_measurements_with_station_names(lists_of_values: <em>list</em>) -&gt; <em>list</em>: lists_of_measurements = []</p>
<p><em>&nbsp;</em></p>
<p><em>for </em>list_of_values <em>in </em>lists_of_values:</p>
<p><em>if </em>'-' <em>in </em>list_of_values <em>or </em>'' <em>in </em>list_of_values: list_of_values.pop()</p>
<p><em>if </em>DataHandler.is_possible_to_fill_missing_data(list_of_values): indexes = DataHandler.get_indexes_for_filling(list_of_values)</p>
<p>list_of_values = DataHandler.fill_missing_data(list_of_values, indexes)</p>
<p><em>else</em>:</p>
<p><em>continue</em></p>
<p>lists_of_measurements.append(DataHandler.get_list_of_float_numbers_and_station(list_of_values))</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>lists_of_measurements</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_lists_of_measurements_with_station_names() </em></p>
<p>This method iterates through lists of values, and if there are '-' or empty spots, these lists are</p>
<p>sent to the special method to be checked if it is possible to fill missing data, and if it is, missing data will be filled. If it is not possible, these lists will not be added to the final data list and then deleted from memory. Before appending list of values to main lists all values are turned to <em>float </em>type in <em>get_list_of_float_numbers_and_station().</em></p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>is_possible_to_fill_missing_data(list_of_values: <em>list</em>) -&gt; <em>bool</em>: index = 0</p>
<p>adder = 1</p>
<p><em>&nbsp;</em></p>
<p><em>while </em>adder &lt; 5 <em>and </em>index &lt; <em>len</em>(list_of_values) - 1 <em>and </em>index + adder &lt; <em>len</em>(list_of_values): <em>if </em>list_of_values[index] == '-' <em>and </em>list_of_values[index + adder] == '-':</p>
<p>adder += 1</p>
<p><em>else</em>:</p>
<p>index += adder adder = 1</p>
<p><em>else</em>:</p>
<p><em>if </em>'' <em>in </em>list_of_values:</p>
<p><em>return False if </em>adder &gt; 4:</p>
<p><em>return False</em></p>
<p><em>elif </em>1 &lt; adder &lt; 5 <em>and </em>adder == <em>len</em>(list_of_values): <em>return False</em></p>
<p><em>else</em>:</p>
<p><em>return True</em></p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of is_possible_to_fill_missing_data() </em></p>
<p>This method simply counts the quantity of missing data in a row, and if there is somewhere in</p>
<p>the list, five and more missing data samples method returns <em>False</em>. It will return <em>False </em>also if</p>
<p>there is just empty string because that means that all list is empty (a feature of the website).</p>
<p>&nbsp;</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_indexes_for_filling(list_of_values: <em>list</em>) -&gt; <em>tuple</em>:</p>
<p><em>&nbsp;</em></p>
<p>index = 0</p>
<p>adder = 1 indexes = []</p>
<p><em>while </em>adder &lt; 5 <em>and </em>index &lt; <em>len</em>(list_of_values) - 1 <em>and </em>index + adder &lt; <em>len</em>(list_of_values): <em>if </em>adder == 1 <em>and </em>list_of_values[index] == '-' <em>and </em>list_of_values[index + 1] != '-':</p>
<p>indexes.append([index, 'one'])</p>
<p><em>&nbsp;</em></p>
<p><em>if </em>list_of_values[index] == '-' <em>and </em>list_of_values[index + adder] == '-': adder += 1</p>
<p><em>elif </em>adder != 1:</p>
<p>indexes.append([index - 1, index + adder, 'normal']) index += adder</p>
<p>adder = 1</p>
<p><em>else</em>:</p>
<p>index += adder adder = 1</p>
<p><em>else</em>:</p>
<p><em>if </em>adder != 1:</p>
<p>indexes.append([index - 1, index + adder, 'in the end'])</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_indexes_for_filling() </em></p>
<p>This method searches for all spots in the list and creates a list of coordinates for another method</p>
<p>to fill missing data later correctly. There are three types of cords: usual Series of missing spots, when only one spot missing data(in real life, there is very little chance that this situation will occur, but I left this variant just in case), and when Series of missing spots are located at the end of the list. How these scenarios are processed is shown in the next method definition.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>fill_missing_data_in_list(list_of_values: <em>list</em>, indexes: <em>tuple</em>) -&gt; <em>list</em>: <em>for </em>index_list <em>in </em>indexes:</p>
<p><em>if </em>index_list[-1] == 'normal':</p>
<p>average = (list_of_values[index_list[0]] + list_of_values[index_list[1]]) / 2</p>
<p><em>&nbsp;</em></p>
<p><em>for </em>i <em>in </em><em>range</em>(index_list[0] + 1, index_list[1]): list_of_values[i] = average</p>
<p><em>elif </em>index_list[-1] == 'one':</p>
<p>average = (list_of_values[index_list[0] - 1] + list_of_values[index_list[0] + 1]) / 2 list_of_values[index_list[0]] = average</p>
<p><em>elif </em>index_list[-1] == 'in the end':</p>
<p><em>for </em>i <em>in </em><em>range</em>(index_list[0], index_list[1]): list_of_values[i] = list_of_values[index_list[0]]</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>list_of_values</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of fill_missing_data_in_list() </em></p>
<p>This method returns the list with filled missing spots. It iterates through a list of coordinates</p>
<p>for filling and depending on coordinates and type of variant of the positioning of missing spots filling occurs.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_list_of_float_numbers_and_station(list_of_values: <em>list</em>) -&gt; <em>list</em>: list_of_data = []</p>
<p><em>&nbsp;</em></p>
<p><em>for </em>value <em>in </em>list_of_values:</p>
<p><em>try</em>:</p>
<p>list_of_data.append(<em>float</em>(value))</p>
<p><em>except </em><em>ValueError</em>: list_of_data.append(value)</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>list_of_data</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_list_of_float_numbers_and_station() </em></p>
<p>The simple method to turn every value in the list from <em>str </em>to <em>float </em>except station name. The</p>
<p>the method returns a new list of data.</p>
<p>&nbsp;</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_station_names(list_of_lists_of_data: <em>list</em>) -&gt; <em>list</em>: list_of_station_names = []</p>
<p><em>&nbsp;</em></p>
<p><em>for </em>list_of_data <em>in </em>list_of_lists_of_data: list_of_station_names.append(list_of_data[-1])</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>list_of_station_names</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_station_names() </em></p>
<p>A simple method that just takes the last element from every list, which is a station name and</p>
<p>appends it to a list of station names.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_lists_of_measurements_without_station_names( list_of_lists_of_measurements_with_station_names: <em>list</em>) -&gt; <em>list</em>:</p>
<p>list_of_lists_of_measurements_without_station_names = []</p>
<p><em>&nbsp;</em></p>
<p><em>for </em>list_of_measurements <em>in </em>list_of_lists_of_measurements_with_station_names: list_of_measurements.pop(<em>len</em>(list_of_measurements) - 1) list_of_lists_of_measurements_without_station_names.append(list_of_measurements)</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>list_of_lists_of_measurements_without_station_names</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_lists_of_measurements_without_station_names() </em></p>
<p>A simple method that iterates through every list deletes the last element of every list, which is</p>
<p>station name and append these lists to the final list that will be returned.</p>
<p>&nbsp;</p>
<h2><a name="_Toc57222448"></a><a name="_Toc57222865"></a>III.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Process data from MySQL</h2>
<p><em>&nbsp;</em></p>
<p>index = DataHandler.get_index_of_value('Dew Point')&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; If needed to estimate data from MySQL database, it first needs to be done to get an index of the value needed to be estimated.</p>
<p>&nbsp;</p>
<p>list_of_measurements = DataHandler.get_exact_value_from_my_sql_records(records, index)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
<p>Now after getting the exact value from records returned from the MySQL database.</p>
<p>IMPORTANT NOTE!</p>
<table width="100%">
<tbody>
<tr>
<td>
<p>records = sql_client.get_info_by_stations(['LV01', 'LV02', 'LV03']) index = DataHandler.get_index_of_value('Dew Point')</p>
<p>lists_of_measurements = DataHandler.get_exact_value_from_many_my_sql_records(records, index)</p>
</td>
</tr>
</tbody>
</table>
<p>If needed to get values from some exact stations, they should use another method to extract value because the previous method is only for processing one station.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p>lists_of_measurements = DataHandler.get_lists_of_floats(lists_of_measurements) list_of_measurements = DataHandler.get_list_of_floats(list_of_measurements)</p>
</td>
</tr>
</tbody>
</table>
<p>Depending on the situation, it should be using the method for process info from one station or many stations.</p>
<p>At this moment, it should have a list of values or lists of values. However, this list/lists may be missing values of type <em>None. </em>A simple method to replace them with a dash of type <em>str, </em>so these lists could be suitable for usage with methods for filling missing data I described earlier.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p>lists_of_measurements = DataHandler.replace_none_with_dash(lists_of_measurements)</p>
</td>
</tr>
</tbody>
</table>
<p>This method accepts a list of lists and returns it after processing.</p>
<p>Now passing lists for filling missing data if it is possible.</p>
<p>&nbsp;</p>
<p>lists_of_measurements = DataHandler.fill_missing_data_in_lists(lists_of_measurements)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
<p>&nbsp;</p>
<p>This method accepts a list of lists as well and returns it. Some details of functionality will be described in the next Definition chapter.</p>
<p>However, in lists that returned are present elements that cannot be used in estimation due to not every list, missing data were filled.</p>
<p>The only option is to check which lists contain <em>str </em>elements, dashes put instead of <em>None, </em>or empty at all and remove them from the main list of measurements. Besides, station codes should be updated because our data needs to be related to the correct station.</p>
<p>station_codes = DataHandler.get_station_codes()&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
<p>The first step &ndash; just create a list of station codes using this simple method.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p>station_codes, lists_of_measurements = DataHandler.zip_codes_and_measurements(station_codes, lists_of_measurements)</p>
</td>
</tr>
</tbody>
</table>
<p>Now passing our lists in the following method, and it will return corrected lists that can be used</p>
<p>in estimation and plot building.</p>
<p>After these manipulations, data is ready for estimation. The process of evaluation is described later.</p>
<p><em>Definitions</em></p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_index_of_value(value: <em>str </em>= 'Dew Point') -&gt; <em>int</em>: <em>if </em>value == 'id':</p>
<p><em>return </em>0</p>
<p><em>elif </em>value == 'Station code':</p>
<p><em>return </em>1</p>
<p><em>elif </em>value == 'Datetime':</p>
<p><em>return </em>2</p>
<p><em>elif </em>value == 'Air Temperature':</p>
<p><em>return </em>3</p>
<p><em>elif </em>value == 'Air Temperature(-1 h)':</p>
<p><em>return </em>4</p>
<p><em>elif </em>value == 'Humidity':</p>
<p><em>return </em>5</p>
<p><em>elif </em>value == 'Dew Point':</p>
<p><em>return </em>6</p>
<p><em>elif </em>value == 'Precipitation':</p>
<p><em>return </em>7</p>
<p><em>elif </em>value == 'Intensity':</p>
<p><em>return </em>8</p>
<p><em>elif </em>value == 'Visibility':</p>
<p><em>return </em>9</p>
<p><em>elif </em>value == 'Road Temperature':</p>
<p><em>return </em>10</p>
<p><em>elif </em>value == 'Road Temperature(-1 h)':</p>
<p><em>return </em>11</p>
<p><em>elif </em>value == 'Road Condition':</p>
<p><em>return </em>12</p>
<p><em>elif </em>value == 'Road Warning':</p>
<p><em>return </em>13</p>
<p><em>elif </em>value == 'Freezing Point':</p>
<p><em>return </em>14</p>
<p><em>elif </em>value == 'Road Temperature 2':</p>
<p><em>return </em>15</p>
<p><em>elif </em>value == 'Road Temperature 2(-1 h)':</p>
<p><em>return </em>16</p>
<p><em>elif </em>value == 'Road Condition 2':</p>
<p><em>return </em>17</p>
<p><em>elif </em>value == 'Road Warning 2':</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_index_of_value() </em></p>
<p>&nbsp;</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>return </em>18</p>
<p><em>elif </em>value == 'Freezing Point 2':</p>
<p><em>return </em>19</p>
</td>
</tr>
</tbody>
</table>
<p>A simple method that returns <em>int </em>as an index of the value passed in argument or which is defined as a default parameter.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_exact_value_from_my_sql_records(records: <em>tuple</em>, index: <em>int</em>) -&gt; <em>list</em>: values = []</p>
<p><em>&nbsp;</em></p>
<p><em>for </em>record <em>in </em>records: values.append(record[index])</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>values</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_exact_value_from_my_sql_records() </em></p>
<p>A simple method that just iterates through records and takes elements by index and adds them</p>
<p>in a list that will be returned in the end.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_exact_value_from_many_my_sql_records(list_of_records: <em>list</em>, index: <em>int</em>) -&gt; <em>list</em>: values = []</p>
<p><em>&nbsp;</em></p>
<p><em>for </em>records <em>in </em>list_of_records: values.append(DataHandler.get_exact_value_from_my_sql_records(records, index))</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>values</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_exact_value_from_many_my_sql_records() </em></p>
<p>This method does the same as the previous one but for records from many stations. Returns list</p>
<p>of lists.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>replace_none_with_dash(lists_of_measurements: <em>list</em>) -&gt; <em>list</em>: i = 0</p>
<p><em>&nbsp;</em></p>
<p><em>for </em>list_of_measurements <em>in </em>lists_of_measurements:</p>
<p><em>for </em>_ <em>in </em>list_of_measurements:</p>
<p><em>if </em>list_of_measurements[i] <em>is None</em>: list_of_measurements[i] = '-'</p>
<p>i += 1</p>
<p>i = 0</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>lists_of_measurements</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of replace_none_with_dash() </em></p>
<p>This simple method just iterates through every element of every row and, if it is <em>None </em>type,</p>
<p>replaces it on '-' character.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>fill_missing_data_in_lists(lists_of_measurements: <em>list</em>) -&gt; <em>list</em>: i = 0</p>
<p><em>for </em>list_of_measurement <em>in </em>lists_of_measurements:</p>
<p><em>if </em>DataHandler.is_possible_to_fill_missing_data(list_of_measurement): indexes = DataHandler.get_indexes_for_filling(list_of_measurement)</p>
<p>list_of_measurement = DataHandler.fill_missing_data_in_list(list_of_measurement, indexes) lists_of_measurements[i] = list_of_measurement</p>
<p>i += 1</p>
<p><em>else</em>:</p>
<p>i += 1</p>
<p><em>return </em>lists_of_measurements</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of fill_missing_data_in_lists() </em></p>
<p>This method iterates through every list and checks if it is possible to fill missing data or not</p>
<p>and if it is, it makes filling using already described methods. IMPORTANT NOTE!</p>
<p>This method works with the whole list at a time, so if there are only one Series of missing data that couldn't be filled, the entire list will be ignored.</p>
<p>&nbsp;</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_station_codes() -&gt; <em>list</em>: station_codes = []</p>
<p><em>&nbsp;</em></p>
<p><em>for </em>i <em>in </em><em>range</em>(1, 65):</p>
<p>station_code = 'LV{:02d}'.format(i) station_codes.append(station_code)</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>station_codes</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_station_codes() </em></p>
<p>This method simply creates a list, fills it with station codes in <em>str </em>type, and returns it in the</p>
<p>result.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>zip_codes_and_measurements(station_codes: <em>list</em>, lists_of_measurements: <em>list</em>) -&gt; <em>tuple</em>: stop = <em>len</em>(lists_of_measurements)</p>
<p>i = 0</p>
<p><em>&nbsp;</em></p>
<p><em>while </em>i &lt; stop:</p>
<p><em>if </em>'-' <em>in </em>lists_of_measurements[i] <em>or not </em><em>bool</em>(lists_of_measurements[i]): lists_of_measurements.pop(i)</p>
<p>station_codes.pop(i) stop -= 1</p>
<p>i = 0</p>
<p><em>else</em>:</p>
<p>i += 1</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>station_codes, lists_of_measurements</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of zip_codes_and_measurements() </em></p>
<p>This method checks every list is it containing dashes or is empty, and if it is, then it deletes this</p>
<p>list from the main list and the corresponding station code from the list of station codes. As a result, modified lists are returned.</p>
<p>&nbsp;</p>
<h2><a name="_Toc57222449"></a><a name="_Toc57222866"></a>IV.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Accuracy</h2>
<p><em>&nbsp;</em></p>
<p>This chapter will be useful after getting familiar with the Estimation chapter because skill is counted using measurements and estimates. The calculation of efficiency is handled by <strong>DataHandler.py</strong>, so that this process will be described here.</p>
<p>Few steps should be made to calculate accuracy:</p>
<ol>
<li>Cast all data values to <em>int </em>type</li>
</ol>
<table width="100%">
<tbody>
<tr>
<td>
<p>lists_of_measurements = DataHandler.get_lists_of_ints(lists_of_measurements)</p>
</td>
</tr>
</tbody>
</table>
<table width="100%">
<tbody>
<tr>
<td>
<p>DataHandler.get_lists_of_ints(lists_of_estimates)</p>
</td>
</tr>
</tbody>
</table>
<table width="100%">
<tbody>
<tr>
<td>
<p>=</p>
</td>
</tr>
</tbody>
</table>
<table width="100%">
<tbody>
<tr>
<td>
<p>lists_of_estimates</p>
</td>
</tr>
</tbody>
</table>
<ol start="2">
<li>Use method, pass lists with data as an argument and will get a list of accuracies</li>
</ol>
<p>accuracies = DataHandler.get_accuracies(lists_of_measurements, lists_of_estimates)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
<p>Now having a list of accuracies of stations that were used in the estimation process.</p>
<p><em>Definitions</em></p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_lists_of_ints(lists_of_values) -&gt; <em>list</em>: <em>for </em>values <em>in </em>lists_of_values:</p>
<p>i = 0</p>
<p><em>while </em>i &lt; <em>len</em>(values): values[i] = <em>int</em>(values[i]) i += 1</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>lists_of_values</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_lists_of_ints() </em></p>
<p>This method iterates through every element of every list and casts it to <em>int</em>.</p>
<p>&nbsp;</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_accuracies(lists_of_measurements: <em>list</em>, lists_of_estimates: <em>list</em>) -&gt; <em>list</em>: accuracies = []</p>
<p><em>for </em>measurements, estimates <em>in </em><em>zip</em>(lists_of_measurements, lists_of_estimates): accuracies.append(DataHandler.get_accuracy(measurements, estimates))</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>accuracies</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_accuracies() </em></p>
<p>This method iterates through every list of measurements, estimates and appends the result of</p>
<p><em>get_accuracy() </em>method, which is described below.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_accuracy(measurements: <em>list</em>, estimates: <em>list</em>) -&gt; <em>float</em>: <em>from </em>sklearn.metrics <em>import </em>accuracy_score</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>accuracy_score(measurements, estimates)</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_accuracy() </em></p>
<p>This method uses a method from <strong>sklearn </strong>module to calculate accuracy and returns the result.</p>
<p>&nbsp;</p>
<h1><a name="_Toc57222450"></a><a name="_Toc57222867"></a>6.&nbsp;&nbsp;&nbsp;&nbsp; ESTIMATION</h1>
<p>For estimation purposes, <strong>KalmanFilter.py </strong>is created with a basic implementation of the Kalman Filter for a one-dimension model.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p>kalman_filter = KalmanFilter(error_in_estimate, initial_estimate, error_in_estimate, measurements)</p>
</td>
</tr>
</tbody>
</table>
<p>The first step is to create a Kalman filter object and pass needed arguments: error in the estimate, an initial estimate, an error in the estimate, and a list of measurements used in the estimation process.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p>estimates = kalman_filter.get_estimates()</p>
</td>
</tr>
</tbody>
</table>
<p>Now it can get a list of estimates by using only one method.</p>
<p>However, if working with a list of lists, they can use the static method from <strong>KalmanFilter.py</strong></p>
<p>that will handle essential processes and return us a list of lists of estimates.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p>lists_of_estimates = KalmanFilter.get_lists_of_estimates(lists_of_measurements, error_in_estimate, error_in_measurement)</p>
</td>
</tr>
</tbody>
</table>
<p>In arguments, passing lists of measurements, errors in the estimate, and error in measurement.</p>
<p>As a result, getting our estimations that can be used for building plots. Plots are described later.</p>
<p><em>Definitions</em></p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em><em>init</em> (<em>self</em>, initial_error_in_estimate, initial_estimate, error_in_measurement,</p>
<p><u>&nbsp; </u>measurements):</p>
<p><em>self</em>.<u>&nbsp; </u>measurements =<u> &nbsp;</u>measurements</p>
<p><em>self</em>.<u>&nbsp; </u>estimate =<u> &nbsp;</u>initial_estimate</p>
<p><em>self</em>. error_in_estimate = initial_error_in_estimate <em>self</em>. error_in_measurement = error_in_measurement <em>self</em>. measurement = <em>None</em></p>
<p><em>self</em>.<u>&nbsp; </u>kalman_gain = <em>None</em></p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of KalmanFilter init () also known as the class constructor </em></p>
<p>This method is just to declare essential variables for the estimation process.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_estimates(<em>self</em>) -&gt; <em>list</em>: list_of_estimates = []</p>
<p><em>&nbsp;</em></p>
<p><em>for </em>measurement <em>in </em><em>self</em>. measurements: <em>self</em>. measurement = measurement <em>self</em>.make_basic_calculations()</p>
<p>list_of_estimates.append(<em>self</em>. estimate)</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>list_of_estimates</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_estimates() </em></p>
<p>This method iterates through all measurements in the list of measurements that are passed when</p>
<p>having been creating the KalmanFilter() object. <em>make_basic_calculations() </em>does what it stands for; its definition is provided below. After every calculation, a new estimate is appended to the list of estimates that will be returned.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>make_basic_calculations(<em>self</em>):</p>
<p><em>self</em>. kalman_gain = <em>self</em>. calculate_kalman_gain() <em>self</em>. estimate = <em>self</em>. calculate_estimate()</p>
<p><em>self</em>. error_in_estimate = <em>self</em>. calculate_error_in_estimate()</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of make_basic_calculations() </em></p>
<p>This method uses other simple methods to produce Kalman Filter calculations for a one-</p>
<p>dimension model and make an estimation. The description of every method is given below.</p>
<p>&nbsp;</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>calculate_kalman_gain(<em>self</em>) -&gt; <em>float</em>:</p>
<p><em>return </em><em>self</em>. error_in_estimate / (<em>self</em>. error_in_estimate + <em>self</em>. error_in_measurement)</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of calculate_kalman_gain() </em></p>
<p><em>&nbsp;</em></p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>calculate_estimate(<em>self</em>) -&gt; <em>float</em>:</p>
<p><em>return </em><em>self</em>. estimate + <em>self</em>. kalman_gain * (<em>self</em>. measurement - <em>self</em>. estimate)</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of calculate_estimate() </em></p>
<p><em>&nbsp;</em></p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>calculate_error_in_estimate(<em>self</em>) -&gt; <em>float</em>:</p>
<p><em>return </em>(1 - <em>self</em>. kalman_gain) * <em>self</em>. error_in_estimate</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of calculate_error_in_estimate() </em></p>
<p><em>&nbsp;</em></p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_lists_of_estimates(lists_of_measurements: <em>list</em>, error_in_estimate: <em>float</em>,</p>
<p>error_in_measurement: <em>float</em>) -&gt; <em>list</em>: lists_of_estimates = []</p>
<p><em>&nbsp;</em></p>
<p><em>for </em>measurements <em>in </em>lists_of_measurements:</p>
<p>initial_estimate = KalmanFilter. get_initial_estimate(measurements)</p>
<p>kf = KalmanFilter(error_in_estimate, initial_estimate, error_in_measurement, measurements) lists_of_estimates.append(kf.get_estimates())</p>
<p><em>&nbsp;</em></p>
<p><em>return </em>lists_of_estimates</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_lists_of_estimates() </em></p>
<p>This method iterates through lists of measurements, automatically creates an initial estimate, KalmanFilter object, and append a list of estimates to the final list that will be returned in the result.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>get_initial_estimate(measurements: <em>list</em>) -&gt; <em>float</em>: <em>return </em>measurements[-1] + (</p>
<p>measurements[-1] - measurements[-2])</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of get_initial_estimate() </em></p>
<p>This method returns an average of the last two elements.</p>
<p>&nbsp;</p>
<h1><a name="_Toc57222451"></a><a name="_Toc57222868"></a>7.&nbsp;&nbsp;&nbsp;&nbsp; PLOTS</h1>
<p>This program has <strong>GraphEditor.py </strong>that uses <strong>matplotlib </strong>module to create plots.</p>
<p>The list of estimates created from plots, it is needed to create an object of <strong><em>class GraphEditor </em></strong>and use correct proper methods:</p>
<table width="100%">
<tbody>
<tr>
<td>
<p>graph = GraphEditor(estimates, measurements, value, station_code, period) graph.create_est_and_meas_plot()</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>Also, there are variants of plots that can be created:</p>
<table width="100%">
<tbody>
<tr>
<td>
<p>graph.create_est_plot() graph.create_meas_plot()</p>
</td>
</tr>
</tbody>
</table>
<p>Creating separate plots for estimates and measurements.</p>
<p>The following method should be used to show plots:</p>
<p>&nbsp;</p>
<p>graph.show_plot()&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
<p>It will display a plot in the program that is used, but if need to save the created plot, this method should be used for saving:</p>
<p>graph.save_plot()&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>IMPORTANT NOTE!</p>
<p>Do not show the plot and then try to save it; it will not work. Separately these methods work just fine.</p>
<p><em>Definitions</em></p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em><em>init</em> (<em>self</em>, estimates: <em>list</em>, measurements: <em>list</em>, value: <em>str</em>, station_name: <em>str</em>, period: <em>str</em>, accuracy=<em>None</em>):</p>
<p><em>self</em>.estimates = estimates <em>self</em>.measurements = measurements <em>self</em>.value = value <em>self</em>.station_name = station_name <em>self</em>.period = period <em>self</em>.accuracy = accuracy <em>self</em>.plt = <em>None</em></p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of GraphEditor init also known as the class constructor </em></p>
<p>Initialization of class object and defining variables.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>create_est_and_meas_plot(<em>self</em>):</p>
<p>plt.plot(<em>self</em>.estimates, label='estimates', color='blue') plt.plot(<em>self</em>.measurements, label='measurements', color='orange') plt.title(<em>self</em>.station_name + ', Period: ' + <em>self</em>.period) plt.ylabel(<em>self</em>.value)</p>
<p>plt.xlabel('Observations') plt.legend()</p>
<p><em>self</em>.plt = plt</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of create_est_and_meas_plot() </em></p>
<p>This method setups settings for plot such as title, legend, labels for x, y axis and saves plot for</p>
<p>further usage like saving or showing in the program.</p>
<p>&nbsp;</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>create_est_plot(<em>self</em>): plt.plot(<em>self</em>.estimates, color='blue')</p>
<p>plt.title('Estimates: ' + <em>self</em>.station_name + ', Period: ' + <em>self</em>.period) plt.ylabel(<em>self</em>.value)</p>
<p>plt.xlabel('Observations')</p>
<p><em>self</em>.plt = plt</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of create_est_plot() </em></p>
<p>This method does the same things but only for estimations.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>create_meas_plot(<em>self</em>): plt.plot(<em>self</em>.measurements, color='orange')</p>
<p>plt.title('Measurements: ' + <em>self</em>.station_name + ', Period: ' + <em>self</em>.period) plt.ylabel(<em>self</em>.value)</p>
<p>plt.xlabel('Observations')</p>
<p><em>self</em>.plt = plt</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of create_meas_plot() </em></p>
<p>This method creates a plot for measurement in a way, like the two previous methods.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>show_plot(<em>self</em>):</p>
<p><em>self</em>.plt.show()</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of</em><em> show_plot() </em></p>
<p>A simple method that shows the plot in the program.</p>
<table width="100%">
<tbody>
<tr>
<td>
<p><em>def </em>save_plot(<em>self</em>): <em>self</em>.plt.savefig('Plot{}.pdf'.format(GraphEditor.index), dpi=300) GraphEditor.index += 1</p>
</td>
</tr>
</tbody>
</table>
<p><br /> <em>Definition of save_plot() </em></p>
<p>A method that saves plot to project folder with settings that were passed as arguments for</p>
<p><em>savefig() </em>method.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<ol start="8">
<li>Forecasting models</li>
</ol>
<p>&nbsp;</p>
<ol>
<li><em>Models</em></li>
</ol>
<p><em>&nbsp;</em></p>
<p>For creating a forecasting model is used <strong>Forecasting_model</strong> class instance, where can be specified model name, steps for making the forecast, optimize value, max p and max q value for models.</p>
<p>&nbsp;</p>
<p><em>Definition of __init__()</em></p>
<p>def __init__(self, model_name, data_series, steps: int, optimize: bool,<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; max_p_value=6, max_q_value=6):<br /> &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; self.model_name = model_name<br /> &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; self.data_series = data_series<br /> &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; self.steps = steps<br /> &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; self.optimize = optimize<br /> <br /> &nbsp;&nbsp;&nbsp; # range (0, 3) == [ 0, 1, 2 ]<br /> &nbsp;&nbsp;&nbsp; if model_name == "ARIMA":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.d_values = range(0, 3)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.p_values = range(0, max_p_value)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.q_values = range(0, max_q_value)<br /> &nbsp;&nbsp;&nbsp; elif model_name == "ARMA":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.d_values = range(0, 1)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.p_values = range(0, max_p_value)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.q_values = range(0, max_q_value)<br /> &nbsp;&nbsp;&nbsp; elif model_name == "AR":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.d_values = range(0, 1)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.q_values = range(0, 1)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.p_values = range(0, max_p_value)<br /> &nbsp;&nbsp;&nbsp; elif model_name == "MA":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.d_values = range(0, 1)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.p_values = range(0, 1)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.q_values = range(0, max_q_value)<br /> &nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.model_name = "Not defined"</p>
<p>&nbsp;</p>
<p><em>&nbsp;</em></p>
<ol>
<li><em>Forecast</em></li>
</ol>
<p>&nbsp;</p>
<p>For making a forecast with the model is used <strong>Forecast_model.py </strong>with modules such as <strong>pandas</strong> for working with data frames and data series, <strong>numpy, </strong>and <strong>ARIMA </strong>from <strong>statsmodels.tsa.arima_model</strong>. For making a forecast and receive all information that was used for forecasting, it is needed to create a class instance and use the correct method as shown here:</p>
<p>arima_data_points, arima_model_order, forecast_arima = Forecasting_model("ARIMA", series_of_measurements, steps, optimize).get_forecast()<br /> <br /> arma_data_points, arma_model_order, forecast_arma = Forecasting_model("ARMA", series_of_measurements, steps, optimize).get_forecast()<br /> <br /> ar_data_points, ar_model_order, forecast_ar = Forecasting_model("AR", series_of_measurements, steps, optimize).get_forecast()<br /> <br /> ma_data_points, ma_model_order, forecast_ma = Forecasting_model("MA", series_of_measurements, steps, optimize).get_forecast()</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>IMPORTANT NOTE!</p>
<p>&nbsp;</p>
<p><em>series_of_measurements</em> must contain only one data column and one index column because for making forecast are used <em>series_of_measurements</em> values, it means it can be used only DataFrame with one data column of just Series.</p>
<p>&nbsp;</p>
<p><em>Definition of </em><em>get_ forecast()</em></p>
<p>def get_forecast(self):<br /> <br /> &nbsp;&nbsp;&nbsp; if self.model_name == "Not defined":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return [None, None, None]<br /> <br /> &nbsp;&nbsp;&nbsp; models_order_and_data_points_dict = self.get_all_possible_models_with_data_points()<br /> <br /> &nbsp;&nbsp;&nbsp; if not bool(models_order_and_data_points_dict):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return [None, None, None]<br /> <br /> &nbsp;&nbsp;&nbsp; # dataframe of data points, steps and RMSE<br /> &nbsp;&nbsp;&nbsp; rmse_df = pd.DataFrame()<br /> <br /> &nbsp;&nbsp; &nbsp;rmse_dict = dict()<br /> &nbsp;&nbsp;&nbsp; last_point = len(self.data_series) - 1 - self.steps<br /> <br /> &nbsp;&nbsp;&nbsp; for data_points, order in models_order_and_data_points_dict.items():<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; first_point = last_point - data_points<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_series_copy = self.data_series[first_point:last_point].copy()<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # ----- Make copy of real data for comparing with forecast ----- #<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_copy_with_steps = self.data_series[last_point - 1:last_point - 1 + self.steps].copy()<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; forecast_list = self.make_forecast(order, data_series_copy, self.steps)<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; rmse = self.get_forecast_accuracy_with_real_data(forecast_list, data_copy_with_steps.values)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; rmse_dict[data_points] = rmse<br /> <br /> &nbsp;&nbsp;&nbsp; rmse_series = pd.Series(rmse_dict)<br /> &nbsp;&nbsp;&nbsp; rmse_df[str(self.steps)] = rmse_series<br /> <br /> &nbsp;&nbsp;&nbsp; rmse_df.reset_index(inplace=True)<br /> &nbsp;&nbsp;&nbsp; rmse_df['order'] = models_order_and_data_points_dict.values()<br /> &nbsp;&nbsp;&nbsp; rmse_df.rename(columns={'index': 'points'}, inplace=True)<br /> &nbsp;&nbsp;&nbsp; rmse_df.set_index(['points', 'order'], inplace=True)<br /> <br /> &nbsp;&nbsp;&nbsp; print(self.model_name)<br /> &nbsp;&nbsp;&nbsp; pd.set_option('display.max_rows', None)<br /> &nbsp;&nbsp;&nbsp; print(rmse_df)<br /> <br /> &nbsp;&nbsp;&nbsp; results = self.get_steps_and_points_of_min_rmse(rmse_df)<br /> <br /> &nbsp;&nbsp;&nbsp; data_points_for_forecast = results[0][0]<br /> <br /> &nbsp;&nbsp;&nbsp; data_series_copy = self.data_series[- data_points_for_forecast:].copy()<br /> <br /> &nbsp;&nbsp;&nbsp; model_order = self.get_order(data_series_copy)<br /> <br /> &nbsp;&nbsp;&nbsp; if model_order is None:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return [None, None, None]<br /> <br /> &nbsp;&nbsp;&nbsp; forecast = self.make_forecast(model_order, data_series_copy, self.steps)<br /> <br /> &nbsp;&nbsp;&nbsp; return [data_points_for_forecast, model_order, forecast]</p>
<p>As a result, we get a list that contains:</p>
<ul>
<li>How many data points must be taken for making a forecast.</li>
<li>ARIMA best model's order (p, d, q).</li>
<li>List of forecast values.</li>
</ul>
<p><em>Definition of get_all_possible_ models_with_data_points()</em></p>
<p>def get_all_possible_models_with_data_points(self):<br /> &nbsp;&nbsp;&nbsp; if self.optimize:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if len(self.data_series) &lt;= 1000 + self.steps:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_optimize_points = len(self.data_series)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; point_range = int(data_optimize_points / 20)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_optimize_points = 1010<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; point_range = 50<br /> &nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_optimize_points = len(self.data_series)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; point_range = int(data_optimize_points / 20)<br /> <br /> &nbsp;&nbsp;&nbsp; models_order_and_data_points_dict = dict()<br /> &nbsp;&nbsp;&nbsp; last_point = len(self.data_series) - self.steps - 1<br /> <br /> &nbsp;&nbsp;&nbsp; data_point_range = range(200, data_optimize_points, point_range)<br /> &nbsp;&nbsp;&nbsp; for data_points in data_point_range:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; first_point = last_point - data_points<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if first_point &lt; 0:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; break<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_series_copy = self.data_series[first_point:last_point].copy()<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; order = self.get_order(data_series_copy)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if order is None:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; continue<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; models_order_and_data_points_dict[data_points] = order<br /> <br /> &nbsp;&nbsp;&nbsp; return models_order_and_data_points_dict</p>
<p>This method returns a dictionary with data points and with the best ARIMA model order for this data set. It looks like this:</p>
<p>{ data_points1 : model_order1, data_points2 : model_order2, &hellip; }</p>
<p>or</p>
<p>{ 100 : [1, 2, 1], 110 : [2, 1, 4] &hellip; }</p>
<p><em>&nbsp;</em></p>
<p><em>&nbsp;</em></p>
<p><em>Definition of get_forecast_accuracy_with_real_data()</em></p>
<p>def get_forecast_accuracy_with_real_data(forecast, actual):<br /> &nbsp;&nbsp;&nbsp; return sqrt(mean_squared_error(actual, forecast))</p>
<p>Returns RMSE as a float value that characterizes the forecast accuracy with actual data</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><em>Definition of</em> <em>make_ forecast ()</em></p>
<p>def make_forecast(order, data_series, steps):<br /> &nbsp;&nbsp;&nbsp; model = ARIMA(data_series, order=order).fit(disp=False)<br /> &nbsp;&nbsp;&nbsp; forecast_list = model.forecast(steps=steps)[0].tolist()<br /> <br /> &nbsp;&nbsp;&nbsp; return forecast_list</p>
<p>The method uses the best ARIMA model order that was found before and returns a forecast value list. The number of received values in the list is equal to the value of the step.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<ul>
<li><em>Model order</em></li>
</ul>
<p>&nbsp;</p>
<p>To determine model order is used with modules <strong>adfuller </strong>test from <strong>statsmodels.tsa.stattools</strong></p>
<p>for finding p-value, that indicates if the model is stationary or not, also can be used <strong>plot_pacf</strong>, <strong>plot_acf </strong>from <strong>statsmodels.graphics.tsaplots </strong>and <strong>pyplot</strong> for showing autocorrelation and partial autocorrelation graphs.</p>
<p>&nbsp;</p>
<p><em>Definition of get_d_value_and_ADF_test()</em></p>
<p>def get_d_value_and_ADF_test(self):<br /> <br /> &nbsp;&nbsp;&nbsp; # ----- Augmented Dickey-Fuller test ----- #<br /> &nbsp;&nbsp;&nbsp; # ----- p-value &gt; 0.05: the data has a unit root and is non-stationary ----- #<br /> &nbsp;&nbsp;&nbsp; # ----- p-value &lt;= 0.05: the data does not have a unit root and is stationary ----- #<br /> &nbsp;&nbsp;&nbsp; # ----- The more negative is ADF Statistic, the more likely we have a stationary dataset ----- #<br /> <br /> &nbsp;&nbsp;&nbsp; d = 0<br /> &nbsp;&nbsp;&nbsp; try:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; adf_test_results = adfuller(self.data_series.values)<br /> &nbsp;&nbsp;&nbsp; except:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return d<br /> <br /> &nbsp;&nbsp;&nbsp; data_series_diff = self.data_series<br /> &nbsp;&nbsp;&nbsp; while adf_test_results[1] &gt; 0.05 or d == 0:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if d &gt; 2:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d += 1<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # ----- make data stationary and drop NA values ----- #<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_series_diff = data_series_diff.diff().dropna()<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; try:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_series_diff_values = data_series_diff.values<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; adf_test_results = adfuller(data_series_diff_values)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; except:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d -= 1<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return d<br /> <br /> &nbsp;&nbsp;&nbsp; return d</p>
<p>This method is used to define the d value for the ARIMA model (p, d, q) order. The d represents the number of times that the data have to be "differenced" to produce a stationary signal (i.e., a signal that has a constant mean over time). This can be captured as the "integrated" nature of ARIMA. If d=0, this means that our data does not tend to go up/down in the long term (i.e., the model is already "stationary"). In this case, then technically, you are performing just ARMA, not AR-I-MA. If p is 1, then it means that the data is going up/down linearly. If p is 2, then it means that the data is going up/down exponentially. To define d value is used&nbsp; Augmented Dickey-Fuller test with p-value:</p>
<ul>
<li>p-value &gt; 0.05: the data has a unit root and is non-stationary.</li>
<li>p-value &lt;= 0.05: the data does not have a unit root and is stationary.</li>
<li>The more negative is ADF Statistic, the more likely we have a stationary dataset.</li>
</ul>
<p>&nbsp;</p>
<p><em>Definition of</em> <em>get _order()</em></p>
<p>def get_order(self, data_series):<br /> &nbsp;&nbsp;&nbsp; aic_dict = dict()<br /> <br /> &nbsp;&nbsp;&nbsp; if len(self.d_values) != 1:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d = self.get_d_value_and_ADF_test()<br /> &nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d = 0<br /> <br /> &nbsp;&nbsp;&nbsp; for p in self.p_values:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for q in self.q_values:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; order = [p, d, q]<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; try:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; arma_model = ARIMA(data_series, order).fit(disp=False)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; aic = arma_model.aic<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if [p, d, q] == [0, 0, 0]:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; continue<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if aic not in aic_dict:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; aic_dict[aic] = order<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # print("Order: {}, AIC: {}".format(order, aic))<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; except:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; continue<br /> <br /> &nbsp;&nbsp;&nbsp; # if aic_dict is empty<br /> &nbsp;&nbsp;&nbsp; # it is impossible to create arima model for this data set<br /> &nbsp;&nbsp;&nbsp; if len(aic_dict) == 0:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return None<br /> <br /> &nbsp;&nbsp;&nbsp; min_val = min(aic_dict.keys())<br /> <br /> &nbsp;&nbsp;&nbsp; return aic_dict[min_val]</p>
<p>This method returns the best model order using the Akaike information criterion for characterizing and d value from <em>d_value_and_ADF_test </em>method. AIC estimates the relative amount of information lost by a given model: the less information a model loses, the higher its quality.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h1>6.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; FORECASTING MODELS</h1>
<p>&nbsp;</p>
<ol>
<li><em>Models</em></li>
</ol>
<p>For creating a forecasting model is used Forecasting_model class instance, where can be specified model name, steps for making forecast, optimize value, max p and max q value for models.</p>
<p>&nbsp;</p>
<p>Definition of __init__()</p>
<p>def __init__(self, model_name, data_series, steps: int, station_code: str,<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; max_p_value=6, max_q_value=6):<br /> <br /> &nbsp;&nbsp;&nbsp; self.model_name = model_name<br /> &nbsp;&nbsp;&nbsp; self.data_series = data_series<br /> &nbsp;&nbsp;&nbsp; self.steps = steps<br /> <br /> &nbsp;&nbsp;&nbsp; if len(self.data_series) &lt;= 100:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; raise Exception("Data must contains more than 100 measurements")<br /> <br /> &nbsp;&nbsp;&nbsp; self.station_code = station_code<br /> <br /> &nbsp;&nbsp;&nbsp; self.min_aic_value = None<br /> &nbsp;&nbsp;&nbsp; self.data_points_to_use = None<br /> &nbsp;&nbsp;&nbsp; self.best_model_order = None<br /> <br /> &nbsp;&nbsp;&nbsp; # range (0, 3) == [ 0, 1, 2 ]<br /> &nbsp;&nbsp;&nbsp; if model_name == "ARIMA":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.d_values = range(0, 3)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.p_values = range(0, max_p_value)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.q_values = range(0, max_q_value)<br /> &nbsp;&nbsp;&nbsp; elif model_name == "ARMA":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.d_values = range(0, 1)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.p_values = range(0, max_p_value)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.q_values = range(0, max_q_value)<br /> &nbsp;&nbsp;&nbsp; elif model_name == "AR":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.d_values = range(0, 1)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.q_values = range(0, 1)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.p_values = range(0, max_p_value)<br /> &nbsp;&nbsp;&nbsp; elif model_name == "MA":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.d_values = range(0, 1)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.p_values = range(0, 1)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.q_values = range(0, max_q_value)<br /> &nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; raise Exception("The model name {} is incorrect".format(model_name))</p>
<p>&nbsp;</p>
<p><em>&nbsp;</em></p>
<ol>
<li><em>Forecast</em></li>
</ol>
<p>For making forecast with model is used <strong>Forecast_model.py </strong>with modules such as <strong>pandas</strong> for working with data frames and data series, <strong>numpy </strong>and <strong>ARIMA </strong>from <strong>statsmodels.tsa.arima_model</strong>. For making forecast and receive all information that was used for forecasting, it is needed to create class instance and use correct method as shown here:</p>
<p>arima_model = ForecastingModel("ARIMA", series_of_measurements, steps, station_code)<br /> forecast_arima = arima_model.get_forecast()<br /> arima_data_points = arima_model.data_points_to_use<br /> arima_model_order = arima_model.best_model_order<br /> <br /> arma_model = ForecastingModel("ARMA", series_of_measurements, steps, station_code)<br /> forecast_arma = arma_model.get_forecast()<br /> arma_data_points = arma_model.data_points_to_use<br /> arma_model_order = arma_model.best_model_order<br /> <br /> ar_model = ForecastingModel("AR", series_of_measurements, steps, station_code)<br /> forecast_ar = ar_model.get_forecast()<br /> ar_data_points = ar_model.data_points_to_use<br /> ar_model_order = ar_model.best_model_order<br /> <br /> ma_model = ForecastingModel("MA", series_of_measurements, steps, station_code)<br /> forecast_ma = ma_model.get_forecast()<br /> ma_data_points = ma_model.data_points_to_use<br /> ma_model_order = ma_model.best_model_order</p>
<p>&nbsp;</p>
<p>IMPORTANT NOTE!</p>
<p>&nbsp;</p>
<p><em>series_of_measurements</em> must contain only one data column and one index column, because for making forecast are used <em>series_of_measurements</em> values.</p>
<p>&nbsp;</p>
<p>Definition of get_ forecast()</p>
<p>def get_forecast(self):<br /> &nbsp;&nbsp;&nbsp; models_for_all_data_points_dict = self.get_possible_models_for_all_data_points_dict()<br /> <br /> &nbsp;&nbsp;&nbsp; self.get_lowest_aic_value_and_data_points_from_dict(models_for_all_data_points_dict)<br /> <br /> &nbsp;&nbsp;&nbsp; if self.data_points_to_use is None:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return None<br /> <br /> &nbsp;&nbsp;&nbsp; data_series_copy = self.data_series[-self.data_points_to_use:].copy()<br /> <br /> &nbsp;&nbsp;&nbsp; forecast = self.make_forecast(data_series_copy)<br /> <br /> &nbsp;&nbsp;&nbsp; return forecast</p>
<p>&nbsp;</p>
<p>As a result we get a list of forecast values.</p>
<p>&nbsp;</p>
<p>Definition of get_possible_models_for_all_data_points_dict()</p>
<p>def get_possible_models_for_all_data_points_dict(self) -&gt; dict:<br /> &nbsp;&nbsp;&nbsp; if len(self.data_series) &lt;= 1000:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_optimize_points = len(self.data_series)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; point_range = int(data_optimize_points / 10)<br /> &nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_optimize_points = 1010<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; point_range = 100<br /> <br /> &nbsp;&nbsp;&nbsp; models_order_and_data_points_dict = dict()<br /> &nbsp;&nbsp;&nbsp; last_point = len(self.data_series)<br /> <br /> &nbsp;&nbsp;&nbsp; data_point_range = range(100, data_optimize_points, point_range)<br /> &nbsp;&nbsp;&nbsp; for data_points in data_point_range:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; first_point = last_point - data_points<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if first_point &lt; 0:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; break<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_series_copy = self.data_series[first_point:last_point].copy()<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; order_and_min_aic_value = self.get_order_and_min_aic_value(data_series_copy)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if order_and_min_aic_value is None:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; continue<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; models_order_and_data_points_dict[data_points] = order_and_min_aic_value<br /> <br /> &nbsp;&nbsp;&nbsp; return models_order_and_data_points_dict</p>
<p>This method returns a dictionary with data points and with the best ARIMA model order for this data set. It looks like this:</p>
<p>{ data_points1 : { (model_order_1) : aic_value_1 }, data_points2 : { (model_order_2) : aic_value_2 }, &hellip; }</p>
<p>or</p>
<p>{ 100 : { (3, 1, 4) : 105 }, 110 : { (4, 1, 4) : 209 } &hellip; }</p>
<p>&nbsp;</p>
<p>Definition of make_ forecast()</p>
<p>def make_forecast(self, data_series):<br /> <br /> &nbsp;&nbsp;&nbsp; model = ARIMA(data_series, order=self.best_model_order).fit(disp=False)<br /> &nbsp;&nbsp;&nbsp; forecast_list = model.forecast(steps=self.steps)[0].tolist()<br /> <br /> &nbsp;&nbsp;&nbsp; return forecast_list</p>
<p>Method uses the best ARIMA model order, that was find before, and returns list of forecast value. The number of received values in the list is equal with steps value.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<ul>
<li><em>Model order</em></li>
</ul>
<p>To determine model order is used with modules <strong>adfuller </strong>test from <strong>statsmodels.tsa.stattools</strong> for finding p-value, that indicates if model is stationary or not, also can be used <strong>plot_pacf</strong>, <strong>plot_acf </strong>from <strong>statsmodels.graphics.tsaplots </strong>and <strong>pyplot</strong> for showing autocorrelation and partial autocorrelation graphs.</p>
<p>&nbsp;</p>
<p>Definition of get_d_value_and_ADF_test()</p>
<p>def get_d_value_and_ADF_test(data_series):<br /> <br /> &nbsp;&nbsp;&nbsp; # ----- Augmented Dickey-Fuller test ----- #<br /> &nbsp;&nbsp;&nbsp; # ----- p-value &gt; 0.05: the data has a unit root and is non-stationary ----- #<br /> &nbsp;&nbsp;&nbsp; # ----- p-value &lt;= 0.05: the data does not have a unit root and is stationary ----- #<br /> &nbsp;&nbsp;&nbsp; # ----- The more negative is ADF Statistic, the more likely we have a stationary dataset ----- #<br /> <br /> &nbsp;&nbsp;&nbsp; d = 0<br /> &nbsp;&nbsp;&nbsp; try:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; adf_test_results = adfuller(data_series.values)<br /> &nbsp;&nbsp;&nbsp; except:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return d<br /> <br /> &nbsp;&nbsp;&nbsp; data_series_diff = data_series<br /> &nbsp;&nbsp;&nbsp; while adf_test_results[1] &gt; 0.05 or d == 0:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if d &gt; 2:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # ----- make data stationary and drop NA values ----- #<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_series_diff = data_series_diff.diff().dropna()<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d += 1<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; try:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_series_diff_values = data_series_diff.values<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; adf_test_results = adfuller(data_series_diff_values)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; except:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d -= 1<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return d<br /> <br /> &nbsp;&nbsp;&nbsp; return d</p>
<p>This method is used to define d value for ARIMA model (p, d , q) order. d represents the number of times that the data have to be &ldquo;differenced&rdquo; to produce a stationary signal (i.e., a signal that has a constant mean over time). This captures the &ldquo;integrated&rdquo; nature of ARIMA. If d=0, this means that our data does not tend to go up/down in the long term (i.e., the model is already &ldquo;stationary&rdquo;). In this case, then technically you are performing just ARMA, not AR-I-MA. If p is 1, then it means that the data is going up/down linearly. If p is 2, then it means that the data is going up/down exponentially. To define d value is used&nbsp; Augmented Dickey-Fuller test with p-value:</p>
<ul>
<li>p-value &gt; 0.05: the data has a unit root and is non-stationary.</li>
<li>p-value &lt;= 0.05: the data does not have a unit root and is stationary.</li>
<li>The more negative is ADF Statistic, the more likely we have a stationary dataset.</li>
</ul>
<p>&nbsp;</p>
<p>Definition of get_order_and_min_aic_value()</p>
<p>def get_order_and_min_aic_value(self, data_series):<br /> &nbsp;&nbsp;&nbsp; aic_dict = dict()<br /> <br /> &nbsp;&nbsp;&nbsp; if len(self.d_values) != 1:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d = self.get_d_value_and_ADF_test(data_series)<br /> &nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d = 0<br /> <br /> &nbsp;&nbsp;&nbsp; for p in self.p_values:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for q in self.q_values:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; order = (p, d, q)<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if order == (0, 0, 0):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; continue<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; try:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; arima_model = ARIMA(data_series, order).fit(disp=False)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; aic = arima_model.aic<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; aic_dict[order] = aic<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # print("Data Points: {}, Order: {}, AIC: {}".format(len(data_series), order, aic))<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; except:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; continue<br /> <br /> &nbsp;&nbsp;&nbsp; # if aic_dict is empty<br /> &nbsp;&nbsp;&nbsp; # it is impossible to create arima model for this data set<br /> &nbsp;&nbsp;&nbsp; if len(aic_dict) == 0:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return None<br /> &nbsp;&nbsp;&nbsp; else:<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; min_aic_val = min(aic_dict.values())<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for key, value in aic_dict.items():<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if value == min_aic_val:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; result_dict = {key: value}<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # order = (p, d, q)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # {order: aic_value }<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return result_dict</p>
<p>This method returns best model order using Akaike information criterion for characterizing and d value from <em>d_value_and_ADF_test </em>method. AIC estimates the relative amount of information lost by a given model: the less information a model loses, the higher the quality of that model</p>
<p>&nbsp;</p>
<h1>7.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; TIME HANDLING</h1>
<p>&nbsp;</p>
<p>Is used to store time valeus and extract data using datetime indexes.</p>
<p>For <strong>TimaHandler.py</strong> is used such modules such as <strong>pandas</strong> for working with data frames and data series, <strong>datime</strong> and <strong>dateutil.relativedelta </strong>for getting datetime values.</p>
<p>&nbsp;</p>
<p>Definition of __init__()</p>
<p>def __init__(self, datetime_unit_of_measure: str, period_value: int,<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; date_from: str = None, date_till: str = None, list_of_datetime: list = None):<br /> <br /> &nbsp;&nbsp;&nbsp; if date_from is None:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if list_of_datetime is None:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; raise Exception("Missing list_of_datetime value")<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.date_from = list_of_datetime[0]<br /> &nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.date_from = self.get_datetime_format(date_from)<br /> <br /> &nbsp;&nbsp;&nbsp; if date_till is None:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if list_of_datetime is None:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; raise Exception("Missing list_of_datetime value")<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.date_till = list_of_datetime[-1]<br /> &nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.date_till = self.get_datetime_format(date_till)<br /> <br /> &nbsp;&nbsp;&nbsp; # datetime delta number<br /> &nbsp;&nbsp;&nbsp; self.period_value = period_value<br /> <br /> &nbsp;&nbsp;&nbsp; # minute, year, second, hour ...<br /> &nbsp;&nbsp;&nbsp; self.datetime_unit_of_measure = datetime_unit_of_measure<br /> &nbsp;&nbsp;&nbsp; # 1 minute<br /> &nbsp;&nbsp;&nbsp; self.datetime_value_of_one_unit = self.get_datetime_value_of_one_unit()<br /> &nbsp;&nbsp;&nbsp; # 11 minutes, 1 hour, 15 days ...<br /> &nbsp;&nbsp;&nbsp; self.datetime_delta_value = self.get_datetime_delta_value()</p>
<p>&nbsp;</p>
<p>Definition of get_datetime_format()</p>
<p>def get_datetime_format(date_time: str):<br /> &nbsp;&nbsp;&nbsp; if len(date_time) == 10:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; date_time += " 00:00:00"<br /> &nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; date_time += ":00"<br /> &nbsp;&nbsp;&nbsp; date_time = datetime.datetime.strptime(date_time, format("%Y-%m-%d %H:%M:%S"))<br /> &nbsp;&nbsp;&nbsp; return date_time</p>
<p>Returns datetime format.</p>
<p>&nbsp;</p>
<p>Definition of <em>get_datetime_from_series ()</em></p>
<p>def get_datetime_from_series(self, data_series, date_from_request):<br /> <br /> &nbsp;&nbsp;&nbsp; max_number_of_iterations = TimeHandler.get_max_number_of_iterations(self.datetime_unit_of_measure)<br /> &nbsp;&nbsp;&nbsp; i = 0<br /> &nbsp;&nbsp;&nbsp; while data_series.loc[data_series.index == date_from_request].empty:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; date_from_request += self.datetime_value_of_one_unit<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i += 1<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if i &gt;= max_number_of_iterations:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return -1<br /> <br /> &nbsp;&nbsp;&nbsp; return date_from_request</p>
<p>By the increasing data_from_request by one datetime_value_of_one_unit program try ti find this datetime index in the series until reach the max nimber of possible iterations.</p>
<p>&nbsp;</p>
<p>Definition of <em>get_max_number_of_iterations()</em></p>
<p>def get_max_number_of_iterations(datetime_unit_of_measure):<br /> &nbsp;&nbsp;&nbsp; if datetime_unit_of_measure == "second":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 60<br /> &nbsp;&nbsp;&nbsp; elif datetime_unit_of_measure == "minute":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 60<br /> &nbsp;&nbsp;&nbsp; elif datetime_unit_of_measure == "hour":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 24<br /> &nbsp;&nbsp;&nbsp; elif datetime_unit_of_measure == "day":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 31<br /> &nbsp;&nbsp;&nbsp; elif datetime_unit_of_measure == "month":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 12<br /> &nbsp;&nbsp;&nbsp; elif datetime_unit_of_measure == "year":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 10<br /> &nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; raise Exception("Parameter time_period_unit must be timedelta value")</p>
<p>Based on <em>datetime_unit_of_measure</em> values returns max number of iterations, that can be used for finding data series datetime index. Without it process of finding datetime index in the series can last forever.</p>
<p>&nbsp;</p>
<p>Definition of <em>get_datetime_value_of_one_unit()</em></p>
<p>def get_datetime_value_of_one_unit(self):<br /> &nbsp;&nbsp;&nbsp; delta_value = 1<br /> &nbsp;&nbsp;&nbsp; if self.datetime_unit_of_measure == "second":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; datetime_value_of_one_unit = datetime.timedelta(seconds=delta_value)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return datetime_value_of_one_unit<br /> &nbsp;&nbsp;&nbsp; elif self.datetime_unit_of_measure == "minute":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; datetime_value_of_one_unit = datetime.timedelta(minutes=delta_value)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return datetime_value_of_one_unit<br /> &nbsp;&nbsp;&nbsp; elif self.datetime_unit_of_measure == "hour":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; datetime_value_of_one_unit = datetime.timedelta(hours=delta_value)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return datetime_value_of_one_unit<br /> &nbsp;&nbsp;&nbsp; elif self.datetime_unit_of_measure == "day":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; datetime_value_of_one_unit = datetime.timedelta(days=delta_value)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return datetime_value_of_one_unit<br /> &nbsp;&nbsp;&nbsp; elif self.datetime_unit_of_measure == "month":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; datetime_value_of_one_unit = dateutil.relativedelta.relativedelta(months=delta_value)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return datetime_value_of_one_unit<br /> &nbsp;&nbsp;&nbsp; elif self.datetime_unit_of_measure == "year":<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; datetime_value_of_one_unit = dateutil.relativedelta.relativedelta(years=delta_value)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return datetime_value_of_one_unit<br /> &nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; raise Exception("Parameter time_period_unit must be timedelta value")</p>
<p>Returns one unit of datetime value.</p>
<p>&nbsp;</p>
<p>Definition of <em>get_datetime_and_measurements_series()</em></p>
<p>def get_datetime_and_measurements_series(self, list_of_measurements, list_of_datetime):<br /> <br /> &nbsp;&nbsp;&nbsp; data_series = pd.Series(list_of_measurements, index=list_of_datetime, dtype=float)<br /> <br /> &nbsp;&nbsp;&nbsp; date_from = self.get_datetime_from_series(data_series, self.date_from)<br /> &nbsp;&nbsp;&nbsp; date_till = self.get_datetime_from_series(data_series, self.date_till)<br /> <br /> &nbsp;&nbsp;&nbsp; if date_from == -1 or date_till == -1:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return pd.Series()<br /> <br /> &nbsp;&nbsp;&nbsp; data_series = data_series.loc[date_from:date_till]<br /> <br /> &nbsp;&nbsp;&nbsp; return data_series</p>
<p>Returns series with datetime index format. If in series can&rsquo;t be found date will bw returned empty series. </p>
<h1>8.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DATA EMPTY VALUES FILLING</h1>
<p>&nbsp;</p>
<p>Is used to fill empty data values &ndash; None or NaN values.</p>
<p>For <strong>DataFiller.py</strong> is used such modules such as <strong>math</strong> for detecting Nan values, <strong>pandas</strong> for working with data frames and data series, <strong>DataHandler</strong>, <strong>MySQLClient</strong> for extracting additional data and <strong>TimeHandler</strong>.</p>
<p>DattaFiller use data from nearest stations, that was defined using clustering method, for filling None or NaN values in the series.</p>
<p>&nbsp;</p>
<p>Definition of __init__()</p>
<p>def __init__(self, data_series, station_clusters_df, station_code,<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; time_handler: TimeHandler, sql_client: MySQLClient):<br /> <br /> &nbsp;&nbsp;&nbsp; self.station_code = station_code<br /> <br /> &nbsp;&nbsp;&nbsp; self.sql_client = sql_client<br /> &nbsp;&nbsp;&nbsp; self.time_handler = time_handler<br /> <br /> &nbsp;&nbsp;&nbsp; self.data_series = data_series<br /> &nbsp;&nbsp;&nbsp; self.station_clusters_df = station_clusters_df</p>
<p>&nbsp;</p>
<p>Definition of get_list_of_stations_codes_to_use()</p>
<p>def get_list_of_stations_codes_to_use(self):<br /> &nbsp;&nbsp;&nbsp; cluster_position = self.station_clusters_df.loc[self.station_code]["cluster"]<br /> &nbsp;&nbsp;&nbsp; stations_to_use = self.station_clusters_df[(self.station_clusters_df["cluster"] == cluster_position)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &amp; (self.station_clusters_df.index != self.station_code)]<br /> <br /> &nbsp;&nbsp;&nbsp; return list(stations_to_use.index)</p>
<p>&nbsp;</p>
<p>Returns list of nearest stations that are located in the same cluster with the station witch data we try to fill.</p>
<p>&nbsp;</p>
<p>Definition of fill_the_data_none_values()</p>
<p>def fill_the_data_none_values(self, value):<br /> &nbsp;&nbsp;&nbsp; stations_codes_to_use_list = self.get_list_of_stations_codes_to_use()<br /> <br /> &nbsp;&nbsp;&nbsp; series_s = []<br /> <br /> &nbsp;&nbsp;&nbsp; for station_code in stations_codes_to_use_list:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; records = self.sql_client.get_info_by_station(station_code)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if not records:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; continue<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_measurements = DataHandler.get_filled_list_of_measurements(records, value)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_datetime = DataHandler.get_exact_value_from_many_my_sql_records([records], 2)[0]<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; series = self.time_handler.get_datetime_and_measurements_series(list_of_measurements, list_of_datetime)<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if not series.empty:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; series_s.append(series)<br /> <br /> &nbsp;&nbsp;&nbsp; for datetime, measurement in self.data_series[self.data_series.isnull()].items():<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; temp_measurement = 0<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i_temp = 0<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for series in series_s:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;temp_datetime = self.time_handler.\<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; get_datetime_from_dataframe_with_delta_limitation(series, datetime, self.time_handler.period_value)<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if temp_datetime != -1:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; temp_value = series.loc[temp_datetime]<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if type(temp_value) == pandas.Series:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; continue<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if temp_value is not None and not math.isnan(temp_value):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; temp_measurement += temp_value<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i_temp += 1<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if i_temp != 0:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; temp_measurement = temp_measurement / i_temp<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.data_series.loc[datetime] = temp_measurement<br /> <br /> &nbsp;&nbsp;&nbsp; return self.data_series</p>
<p>Goes through fo all data series that are located in the same cluster and extracts data value with the same datetime index or with the datetime index that was taken shortly before (in this way in used limitation for finding datetime index from <strong>TimeHandler</strong>)</p>
<p>As a result returns series with filled data points.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h1>9.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; CLUSTERING</h1>
<p>&nbsp;</p>
<p>Clustering method is used for <strong>DataFiller</strong> for finding the stations. That are located in the one cluster. In the <strong>Cluster.py</strong> is used modeles such as <strong>KMeans</strong> for clustering algorithm that aims to partition n observations into <strong>k</strong> clusters, <strong>MinMaxScaler</strong> for transforming features by scaling each feature to a given range (This estimator scales and translates each feature individually such that it is in the given range on the training set, e.g. between zero and one), <strong>math</strong> for finding square root, <strong>pandas</strong> and <strong>numpy</strong>.</p>
<p>Definition of __init__()</p>
<p>def __init__(self, records, max_k_value=10, default_k_value=None, path_to_save_results=None):<br /> &nbsp;&nbsp;&nbsp; self.k_range = range(1, max_k_value)<br /> &nbsp;&nbsp;&nbsp; self.records_df = self.get_records_df(records)<br /> &nbsp;&nbsp;&nbsp; self.lat_and_lng_array = self.get_lat_and_lng_array()<br /> <br /> &nbsp;&nbsp;&nbsp; self.path_to_save_results = path_to_save_results<br /> &nbsp;&nbsp;&nbsp; if path_to_save_results is not None:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.save_results = True<br /> &nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.save_results = False<br /> <br /> &nbsp;&nbsp;&nbsp; self.default_k_value = default_k_value<br /> <br /> &nbsp;&nbsp;&nbsp; self.dist_points_from_cluster_center = None<br /> &nbsp;&nbsp;&nbsp; self.distance_of_points_from_line = None<br /> <br /> &nbsp;&nbsp;&nbsp; if default_k_value is None:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.optimal_k_value = self.get_optimal_k_value()<br /> &nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.optimal_k_value = default_k_value</p>
<p>For the rocords value is used data with station codes and with latitude and longitude for each station. As a default value of <em>max_k_value</em> used integer 10. If <em>default_k_value</em> is not specified algorithm automatically finds the <em>optimal_k_value</em>.</p>
<p>&nbsp;</p>
<p>Definition of <em>get_records_df()</em></p>
<p>def get_records_df(records):<br /> &nbsp;&nbsp;&nbsp; records_df = pd.DataFrame.from_records(records, columns=["index", "code", "name", "lat", "lng"])<br /> &nbsp;&nbsp;&nbsp; records_df = records_df[["code", "lat", "lng"]]<br /> <br /> &nbsp;&nbsp;&nbsp; records_df["lat"] = records_df["lat"].astype(float)<br /> &nbsp;&nbsp;&nbsp; records_df["lng"] = records_df["lng"].astype(float)<br /> <br /> &nbsp;&nbsp;&nbsp; return records_df</p>
<p>Returns a data frame with all stations with latitude and longitude as float numbers.</p>
<p>&nbsp;</p>
<p>Definition of <em>get_lat_and_lng_array()</em></p>
<p>def get_lat_and_lng_array(self):<br /> &nbsp;&nbsp;&nbsp; lat_and_lng_array = np.column_stack((self.records_df["lng"], self.records_df["lat"]))<br /> &nbsp;&nbsp;&nbsp; return lat_and_lng_array</p>
<p>Returns 2D array for latitude and longitude using records data frame.</p>
<p>&nbsp;</p>
<p>Definition of <em>get_optimal_k_value()</em></p>
<p>def get_optimal_k_value(self):<br /> &nbsp;&nbsp;&nbsp; self.dist_points_from_cluster_center = self.get_dist_points_from_cluster_center_using_k_range()<br /> &nbsp;&nbsp;&nbsp; self.distance_of_points_from_line = self.cal_distance_of_points_from_line()<br /> <br /> &nbsp;&nbsp;&nbsp; opt_value = self.distance_of_points_from_line.index(max(<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; self.distance_of_points_from_line)) + 1<br /> &nbsp;&nbsp;&nbsp; return opt_value</p>
<p>Return the <em>optimal_k_value</em>.</p>
<p>&nbsp;</p>
<p>Definition of <em>make_clustering()</em></p>
<p>def make_clustering(self):<br /> &nbsp;&nbsp;&nbsp; km = KMeans(n_clusters=self.optimal_k_value)<br /> &nbsp;&nbsp;&nbsp; predicted = km.fit_predict(self.records_df[["lng", "lat"]])<br /> &nbsp;&nbsp;&nbsp; self.records_df["cluster"] = predicted</p>
<p>Make clustering and returns a data frame with station codes and with cluster nuber for each station.</p>
<p>Definition of <em>make_scaler()</em></p>
<p>def make_scaler(self):<br /> &nbsp;&nbsp;&nbsp; scaler = MinMaxScaler()<br /> <br /> &nbsp;&nbsp;&nbsp; scaler.fit(self.records_df[["lat"]])<br /> &nbsp;&nbsp;&nbsp; self.records_df["lat"] = scaler.transform(self.records_df[["lat"]])<br /> <br /> &nbsp;&nbsp;&nbsp; scaler.fit(self.records_df[["lng"]])<br /> &nbsp;&nbsp;&nbsp; self.records_df["lng"] = scaler.transform(self.records_df[["lng"]])</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h1>10.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; KALMAN FILTER 1D AND 2D</h1>
<p>&nbsp;</p>
<p>For data smoothing is used Kalman Filter from <strong>KF.py</strong>. When datac is one-dimensional it can be used class <strong>KF_1D </strong>and when your data contains position and velocity (x, v) must be used class <strong>KF_2D</strong>. For using with Kalman Filter must be installed modules such as <strong>pykalman</strong>.</p>
<p>&nbsp;</p>
<ol>
<li><em>One-dimensional Kalman Filter </em></li>
</ol>
<p>For getting smoothed values must be used class <strong>KF_1D </strong>and as a input paramentrs must be used list of measurements:</p>
<p>filtered_values = KF_1D(list_of_measurements).get_filtered_values()</p>
<p>&nbsp;</p>
<p>Definition of get_filtered_values()</p>
<p>def get_filtered_values(self):<br /> <br /> &nbsp;&nbsp;&nbsp; kf = KalmanFilter(transition_matrices=[1],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; observation_matrices=[1],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; initial_state_mean=0,<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; initial_state_covariance=1,<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; observation_covariance=1,<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; transition_covariance=0.05)<br /> <br /> &nbsp;&nbsp;&nbsp; state_means, state_covariances = kf.smooth(self.data_values_list)<br /> <br /> &nbsp;&nbsp;&nbsp; state_means_list = [state_mean[0] for state_mean in state_means]<br /> <br /> &nbsp;&nbsp;&nbsp; return state_means_list</p>
<p>&nbsp;</p>
<p>Returns a list of smoothed values.</p>
<p>&nbsp;</p>
<ol>
<li><em>Two-dimensiona</em><em>l Kalman Filter </em></li>
</ol>
<p>For getting smoothed values with position and velocity (x, v) )must be used class <strong>KF_2D </strong>and as a input paramentrs must be used list of measurements, starting position, starting velocity and period of time when data was measured (time_delta):</p>
<p>filtered_values = KF_2D(list_of_measurements, position=position, velocity=velocity,<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; time_delta=time_delta).get_filtered_values()</p>
<p><em>&nbsp;</em></p>
<p>Definition of get_filtered_values ()</p>
<p>def get_filtered_values(self):<br /> <br /> &nbsp;&nbsp;&nbsp; kf = KalmanFilter(n_dim_obs=1, n_dim_state=2,<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; initial_state_mean=[self.position, self.velocity],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; transition_matrices=[[1, self.time_delta], [0, 1]],&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; observation_matrices=[[1, 0]],&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; transition_offsets=[0.5 * self.time_delta ** 2, self.time_delta])<br /> <br /> &nbsp;&nbsp;&nbsp; state_means, state_covariances = kf.smooth(self.data_values_list)<br /> <br /> &nbsp;&nbsp;&nbsp; state_means_list = [state_mean[0] for state_mean in state_means]<br /> <br /> &nbsp;&nbsp;&nbsp; return state_means_list</p>
<p><em>&nbsp;</em></p>
<p><em>&nbsp;</em></p>
<p>For the two-dimensional Kalman Filter is used:</p>
<ul>
<li>initial_state_mean or <strong>x<sub>k</sub></strong> as a (x, v)</li>
<li>transition_matrices or <strong>F</strong> as a matrix form of [[1, self.time_delta], [0, 1]]</li>
<li>observation_matrices or <strong>H</strong> as a vector form of [[1, 0]]</li>
<li>transition_offsets or <strong>G</strong> as a mtrix form of [0.5 * self.time_delta ** 2, self.time_delta]</li>
</ul>
<p>Returns a list of smoothed values.</p>
<p><em><br /> </em></p>
<p><em>&nbsp;</em></p>
<p><em>&nbsp;</em></p>
<h1>11.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; API</h1>
<p>The fundamental representation of API that can be used as Web Service of this framework. Twelve routes are used:</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /use/1d_kalman_filter</p>
<p>&nbsp;</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /use/2d_kalman_filter</p>
<p>&nbsp;</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /get/forecast</p>
<p>&nbsp;</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /get/forecast/time_period</p>
<p>&nbsp;</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /get/forecast/all_models</p>
<p>&nbsp;</p>
<p>All these requests have essential arguments and secondary ones. Every request has an essential argument <em>value</em>.</p>
<p>&nbsp;</p>
<h2>I.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /use/1d_kalman_filter</h2>
<p>Is used for getting smoothed values using one-dimensional Kalman Filter .</p>
<p>Essential arguments: value, station, datetime_unit_of_measure, period_value.</p>
<p>For <em>value</em> argumest can be used &ldquo;Dew Point&rdquo;, &ldquo;Air Temperature&rdquo; and etc.</p>
<p>For <em>datetime_unit_of_measure </em>must be used <u>str</u> value, that defines unit of measure of time delta value (&ldquo;second&rdquo;, &ldquo;minute&rdquo;, &ldquo;hour&rdquo;, &ldquo;day&rdquo;, &ldquo;month&rdquo;, &ldquo;year&rdquo;)</p>
<p>For <em>period_value </em>must be used <u>int</u> value, that defines delta value.</p>
<p>If <em>period_value</em> is 11 and <em>datetime_unit_of_measure is </em>&ldquo;minute&rdquo;, it means delta value will be 11 minutes.</p>
<p><em>For example:</em></p>
<p><a href="http://127.0.0.1/use/1d_kalman_filter?station=LV01&amp;value=Dew%20Point">/use/1d_kalman_filter?station=LV01&amp;value=Dew%20Point</a>&amp;<u>datetime_unit_of_measure</u><u>=minute&amp;period_value=11</u></p>
<p>&nbsp;</p>
<h2>II.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /use/2d_kalman_filter</h2>
<p>Is used for getting smoothed values using two-dimensional Kalman Filter .</p>
<p>Essential arguments: value, station, datetime_unit_of_measure, period_value.</p>
<p>For <em>value</em> argumest can be used &ldquo;Dew Point&rdquo;, &ldquo;Air Temperature&rdquo; and etc.</p>
<p>Secondary argument: position, velocity and time_delta</p>
<p>As a default values for secondary arguments:</p>
<p>position = 0</p>
<p>velocity = 0</p>
<p>time_delta = 0.1</p>
<p>&nbsp;</p>
<p>For <em>datetime_unit_of_measure </em>must be used <u>str</u> value, that defines unit of measure of time delta value (&ldquo;second&rdquo;, &ldquo;minute&rdquo;, &ldquo;hour&rdquo;, &ldquo;day&rdquo;, &ldquo;month&rdquo;, &ldquo;year&rdquo;)</p>
<p>For <em>period_value </em>must be used <u>int</u> value, that defines delta value.</p>
<p>If <em>period_value </em>is 11 and <em>datetime_unit_of_measure is </em>&ldquo;minute&rdquo;, it means delta value will be 11 minutes.</p>
<p><em>For example:</em></p>
<p><a href="http://127.0.0.1/use/1d_kalman_filter?station=LV01&amp;value=Dew%20Point">/use/2d_kalman_filter?station=LV01&amp;value=Dew%20Point</a>&amp;<u>datetime_unit_of_measure</u><u>=minute&amp;period_value=11</u></p>
<p>In this case will be used default values for secondary arguments. This request will return JSON with smoothed values for stations and value that are set up in request arguments.</p>
<p><u>/use/2d_kalman_filter?station=LV01&amp;value=Dew%20Point&amp;position=1&amp;velocity=9&amp;time_delta=0.2&amp;datetime_unit_of_measure=minute&amp;period_value=11</u></p>
<p>&nbsp;</p>
<h2>III.&nbsp;&nbsp;&nbsp; /get/forecast</h2>
<p>Is used for getting forecast values using station data.</p>
<p>Essential arguments: model_name, value, station, steps, datetime_unit_of_measure, period_value.</p>
<p>Secondary arguments: using_Kalman_Filter.</p>
<p>For the <em>model_name </em>value can be used ARIMA, ARMA, AR and MA models.</p>
<p>For <em>value</em> argumest can be used &ldquo;Dew Point&rdquo;, &ldquo;Air Temperature&rdquo; and etc.</p>
<p><em>Steps</em> value means how many points ahead will be made forecast.</p>
<p>For <em>datetime_unit_of_measure </em>must be used <u>str</u> value, that defines unit of measure of time delta value (&ldquo;second&rdquo;, &ldquo;minute&rdquo;, &ldquo;hour&rdquo;, &ldquo;day&rdquo;, &ldquo;month&rdquo;, &ldquo;year&rdquo;)</p>
<p>For <em>period_value </em>must be used <u>int</u> value, that defines delta value.</p>
<p>If <em>period_value </em>is 11 and <em>datetime_unit_of_measure is </em>&ldquo;minute&rdquo;, it means delta value will be 11 minutes.</p>
<p>For the value <em>using_Kalman_Filter </em>must be used only True or False values.</p>
<p><em>For example:</em></p>
<p><a href="http://127.0.0.1/get/forecast/arima?value=Dew%20Point&amp;station=LV01&amp;steps=5&amp;optimize=true">/get/forecast?model_name=ARIMA&amp;value=Dew%20Point&amp;station=LV01&amp;steps=5&amp;</a><u>datetime_unit_of_measure</u><u>=minute&amp;period_value=11</u></p>
<p><a href="http://127.0.0.1/get/forecast/arima?value=Dew%20Point&amp;station=LV01&amp;steps=5&amp;optimize=true">/get/forecast?model_name=AR&amp;value=Dew%20Point&amp;station=LV06&amp;steps=10&amp;</a><u>datetime_unit_of_measure</u><u>=hour&amp;period_value=1&amp;using_Kalman_Filter=True</u></p>
<p>&nbsp;</p>
<h2>IV.&nbsp;&nbsp;&nbsp;&nbsp; /get/forecast/time_period</h2>
<p>Is used for getting forecast values using station data and using time period with date from and date till.</p>
<p>Essential argument: model_name , value, station, steps, datetime_unit_of_measure, period_value.</p>
<p>Secondary arguments: using_Kalman_Filter.</p>
<p>For the <em>model_name </em>value can be used ARIMA, ARMA, AR and MA models.</p>
<p>For <em>datetime_unit_of_measure </em>must be used <u>str</u> value, that defines unit of measure of time delta value (&ldquo;second&rdquo;, &ldquo;minute&rdquo;, &ldquo;hour&rdquo;, &ldquo;day&rdquo;, &ldquo;month&rdquo;, &ldquo;year&rdquo;)</p>
<p>For <em>period_value </em>must be used <u>int</u> value, that defines delta value.</p>
<p>If <em>period_value </em>is 11 and <em>datetime_unit_of_measure is </em>&ldquo;minute&rdquo;, it means delta value will be 11 minutes.</p>
<p>For the value <em>using_Kalman_Filter </em>must be used only True or False values.</p>
<p>Date value can be inputed in two formats:</p>
<ul>
<li>YYYY-MM-DD and time value will be automatically set to 00:00</li>
<li>YYYY-MM-DD_HH:MM</li>
</ul>
<p><em>For example:</em></p>
<p><a href="http://127.0.0.1/get/forecast/arima/time_period?value=Dew%20Point&amp;station=LV01&amp;steps=5&amp;optimize=true&amp;date_from=2020-02-10_12:00&amp;date_till=2020-04-15_14:00">/get/forecast/time_period?model_name=ARMA&amp;value=Dew%20Point&amp;station=LV01&amp;steps=5&amp;date_from=2020-02-10_12:00&amp;date_till=2020-04 15_14:00</a><u>&amp;datetime_unit_of_measure</u><u>=minute&amp;period_value=11</u></p>
<p><a href="http://127.0.0.1/get/forecast/arima/time_period?value=Dew%20Point&amp;station=LV01&amp;steps=5&amp;optimize=true&amp;date_from=2020-02-10&amp;date_till=2020-04-15">/get/forecast/time_period?model_name=ARIMA&amp;value=Dew%20Point&amp;station=LV05&amp;steps=5&amp;date_from=2020-02-10&amp;date_till=2020-04-15</a><u>&amp;datetime_unit_of_measure</u><u>=minute&amp;period_value=11&amp;using_Kalman_Filter=True</u></p>
<p>&nbsp;</p>
<h2>V.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /get/forecast/all_models</h2>
<p>Is used for getting forecast values using station data for all models (ARIMA, ARMA, AR, MA) usind one-dimensional .</p>
<p>Essential argument: value, station, steps datetime_unit_of_measure, period_value.</p>
<p>Secondary arguments: using_Kalman_Filter.</p>
<p>For <em>value</em> argumest can be used &ldquo;Dew Point&rdquo;, &ldquo;Air Temperature&rdquo; and etc.</p>
<p><em>Steps</em> value means how many points ahead will be made forecast.</p>
<p>For <em>datetime_unit_of_measure </em>must be used <u>str</u> value, that defines unit of measure of time delta value (&ldquo;second&rdquo;, &ldquo;minute&rdquo;, &ldquo;hour&rdquo;, &ldquo;day&rdquo;, &ldquo;month&rdquo;, &ldquo;year&rdquo;)</p>
<p>For <em>period_value </em>must be used <u>int</u> value, that defines delta value.</p>
<p>If <em>period_value </em>is 11 and <em>datetime_unit_of_measure is </em>&ldquo;minute&rdquo;, it means delta value will be 11 minutes.</p>
<p>For the value <em>using_Kalman_Filter </em>must be used only True or False values.</p>
<p><em>For example:</em></p>
<p><a href="http://127.0.0.1/get/forecast/arima?value=Dew%20Point&amp;station=LV01&amp;steps=5&amp;optimize=true">/get/forecast/all_models?value=Dew%20Point&amp;station=LV01&amp;steps=5</a><u>&amp;datetime_unit_of_measure</u><u>=minute&amp;period_value=11</u></p>
<p><a href="http://127.0.0.1/get/forecast/arima?value=Dew%20Point&amp;station=LV01&amp;steps=5&amp;optimize=true">/get/forecast/all_models?value=Dew%20Point&amp;station=LV01&amp;steps=5</a><u>&amp;datetime_unit_of_measure</u><u>=minute&amp;period_value=11&amp;using_Kalman_Filter=True</u></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
