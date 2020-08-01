<h1>Autonomous Open Data Prediction Framework</h1>
<p>&nbsp;</p>
<p>Documentation</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>Riga Technical University</p>
<p>Faculty of Computer Science and Information Technology</p>
<p>Information Technology Institute</p>
<p>Department of Management Information Technology</p>
<p><strong>Jānis Pek&scaron;a</strong></p>
<p>Research Assistant</p>
<p><a href="http://iti.rtu.lv/vitk/lv/katedra/darbinieki/janis-peksa">http://iti.rtu.lv/vitk/lv/katedra/darbinieki/janis-peksa</a></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><strong>INDEX</strong></p>
<ol>
<li><a href="#_Toc47164640"> Introduction. 5</a></li>
<li><a href="#_Toc47164641"> Website Connection. 6</a></li>
</ol>
<p><a href="#_Toc47164642">Definitions: 6</a></p>
<p><a href="#_Toc47164643">Definition of get_table() 6</a></p>
<p><a href="#_Toc47164644">Definition of get_data_lists_from_table() 7</a></p>
<ol start="3">
<li><a href="#_Toc47164645"> MySQL Connection. 8</a></li>
</ol>
<p><a href="#_Toc47164646">Definitions. 8</a></p>
<p><a href="#_Toc47164647">Definition of MySQLClient __init__() also known as class constructor 8</a></p>
<p><a href="#_Toc47164648">Definition of MySQLClient connect_to_database() 8</a></p>
<p><a href="#_Toc47164649">Definition of get_all_info_from_database() 9</a></p>
<p><a href="#_Toc47164650">Definition of get_info_by_station() 9</a></p>
<p><a href="#_Toc47164651">Definition of get_info_by_stations() 9</a></p>
<ol start="4">
<li><a href="#_Toc47164652"> MongoDB Connection. 10</a></li>
<li><a href="#_Toc47164653"> Difference between database clients. 10</a></li>
</ol>
<p><a href="#_Toc47164654">Definitions. 10</a></p>
<p><a href="#_Toc47164655">Definition of MongoDBClient __init__() also known as class constructor 10</a></p>
<p><a href="#_Toc47164656">Definition of get_connection() 10</a></p>
<ol>
<li><a href="#_Toc47164657"> MongoDB Importing. 10</a></li>
</ol>
<p><a href="#_Toc47164658">Definitions. 11</a></p>
<p><a href="#_Toc47164659">Definition of get_all_info_from_main_database() 11</a></p>
<p><a href="#_Toc47164660">Definition of get_data_from_collection() 11</a></p>
<p><a href="#_Toc47164661">Definition of get_data_from_collections() 12</a></p>
<p><a href="#_Toc47164662">III.&nbsp;&nbsp;&nbsp; MongoDB Exporting. 12</a></p>
<ol start="5">
<li><a href="#_Toc47164663"> Data Handling. 13</a></li>
<li><a href="#_Toc47164664"> For exporting to MongoDB.. 13</a></li>
</ol>
<p><a href="#_Toc47164665">Definitions. 13</a></p>
<p><a href="#_Toc47164666">Definition of get_data_dicts() 13</a></p>
<p><a href="#_Toc47164667">Definition of get_date() 13</a></p>
<ol>
<li><a href="#_Toc47164668"> Process data from MongoDB.. 14</a></li>
</ol>
<p><a href="#_Toc47164669">Data from MongoDB database. 14</a></p>
<p><a href="#_Toc47164670">Definitions. 14</a></p>
<p><a href="#_Toc47164671">Definition of get_prepared_lists_for_estimation() 14</a></p>
<p><a href="#_Toc47164672">Definition of get_lists_of_chosen_values_with_station_names() 14</a></p>
<p><a href="#_Toc47164673">Definition of get_lists_of_measurements_with_station_names() 15</a></p>
<p><a href="#_Toc47164674">Definition of is_possible_to_fill_missing_data() 15</a></p>
<p><a href="#_Toc47164675">Definition of get_indexes_for_filling() 16</a></p>
<p><a href="#_Toc47164676">Definition of fill_missing_data_in_list() 16</a></p>
<p><a href="#_Toc47164677">Definition of get_list_of_float_numbers_and_station() 16</a></p>
<p><a href="#_Toc47164678">Definition of get_station_names() 17</a></p>
<p><a href="#_Toc47164679">Definition of get_lists_of_measurements_without_station_names() 17</a></p>
<p><a href="#_Toc47164680">III.&nbsp;&nbsp;&nbsp; Process data from MySQL. 17</a></p>
<p><a href="#_Toc47164681">Definitions. 18</a></p>
<p><a href="#_Toc47164682">Definition of get_index_of_value() 18</a></p>
<p><a href="#_Toc47164683">Definition of get_exact_value_from_my_sql_records() 19</a></p>
<p><a href="#_Toc47164684">Definition of get_exact_value_from_many_my_sql_records() 19</a></p>
<p><a href="#_Toc47164685">Definition of replace_none_with_dash() 19</a></p>
<p><a href="#_Toc47164686">Definition of fill_missing_data_in_lists() 19</a></p>
<p><a href="#_Toc47164687">Definition of get_station_codes() 20</a></p>
<p><a href="#_Toc47164688">Definition of zip_codes_and_measurements() 20</a></p>
<ol>
<li><a href="#_Toc47164689"> Accuracy. 20</a></li>
</ol>
<p><a href="#_Toc47164690">Definitions. 20</a></p>
<p><a href="#_Toc47164691">Definition of get_lists_of_ints() 20</a></p>
<p><a href="#_Toc47164692">Definition of get_accuracies() 21</a></p>
<p><a href="#_Toc47164693">Definition of get_accuracy() 21</a></p>
<ol start="6">
<li><a href="#_Toc47164694"> Estimation. 22</a></li>
</ol>
<p><a href="#_Toc47164695">Definitions. 22</a></p>
<p><a href="#_Toc47164696">Definition of KalmanFilter __init__() also known as class constructor 22</a></p>
<p><a href="#_Toc47164697">Definition of get_estimates() 22</a></p>
<p><a href="#_Toc47164698">Definition of make_basic_calculations() 22</a></p>
<p><a href="#_Toc47164699">Definition of __calculate_kalman_gain() 23</a></p>
<p><a href="#_Toc47164700">Definition of __calculate_estimate() 23</a></p>
<p><a href="#_Toc47164701">Definition of __calculate_error_in_estimate() 23</a></p>
<p><a href="#_Toc47164702">Definition of get_lists_of_estimates() 23</a></p>
<p><a href="#_Toc47164703">Definition of __get_initial_estimate() 23</a></p>
<ol start="7">
<li><a href="#_Toc47164704"> Plots. 24</a></li>
</ol>
<p><a href="#_Toc47164705">Definitions. 24</a></p>
<p><a href="#_Toc47164706">Definition of GraphEditor __init__ also known as class constructor 24</a></p>
<p><a href="#_Toc47164707">Definition of create_est_and_meas_plot() 24</a></p>
<p><a href="#_Toc47164708">Definition of create_est_plot() 25</a></p>
<p><a href="#_Toc47164709">Definition of create_meas_plot() 25</a></p>
<p><a href="#_Toc47164710">Definition of show_plot() 25</a></p>
<p><a href="#_Toc47164711">Definition of save_plot() 25</a></p>
<ol start="8">
<li><a href="#_Toc47164712"> ARIMA.. 26</a></li>
<li><a href="#_Toc47164713"> ARIMA main. 26</a></li>
<li><a href="#_Toc47164714"> ARIMA order 28</a></li>
<li><a href="#_Toc47164715"> API 31</a></li>
<li><a href="#_Toc47164716"> /get/estimates/all 31</a></li>
<li><a href="#_Toc47164717"> /get/estimates 31</a></li>
</ol>
<p><a href="#_Toc47164718">III.&nbsp;&nbsp;&nbsp; /get/accuracies. 32</a></p>
<ol>
<li><a href="#_Toc47164719"> /get/forecast/arima. 32</a></li>
<li><a href="#_Toc47164720"> /get/forecast/arima/time_period. 32</a></li>
</ol>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h1><a name="_Toc47164640"></a><a name="_Toc33784662"></a>1.&nbsp;&nbsp;&nbsp; Introduction</h1>
<p>This is the detailed documentation of the program, which is part of the Autonomous Open Data Prediction Framework. Here are described methods to implement all essential functionality. Some of the methods aren&rsquo;t described because they are built-in in Python or taken from Python modules. It will be announced if some of Python files described below use other modules for Python. All these functions, methods, and modules written not by me have their references, description, and examples of usage on the Internet. All of them can be used freely, as provided and without almost any limitations.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h1><a name="_Toc47164641"></a><a name="_Toc33784663"></a>2.&nbsp;&nbsp;&nbsp; Website Connection</h1>
<p>The first source of data is the website www.lvceli.lv/cms. The <strong>Request.py </strong>to implement the needed functionality. At the core of it are such modules as <strong>requests </strong>and<strong> BeautifoulSoup. </strong>First, one is needed to make GET/POST requests to the website and the second one is needed to process HTML properly which is returned by requests.o</p>
<p>Examples of using and explanation:</p>
<p>table = Request.get_table()</p>
<p>&nbsp;</p>
<p>Firstly, to get a table from the website. This method does everything it needs to return the correct table with observations that it contains. No need to pass the URL of the website because it&rsquo;s given as a default parameter, as shown in the definition below. Now to have a table with data, but before need to separate values from HTML because this method only returns part of the webpage.</p>
<p>data_lists = Request.get_data_lists_from_table(table)</p>
<p>&nbsp;</p>
<p>Now using another method that will extract all data from HTML, save it to lists and return a list of records like [[], [], []].</p>
<p>This data program can process correctly, export to the database and make estimations but before this operations, some more functionality will be described to understand what is going on inside fully.</p>
<p>Because working with databases to store vast amounts of data, this module is crucial for gathering data in real-time and has some simple methods to work with. Still, it is much more convenient to import/export data using clients of databases that are described next.</p>
<h3><a name="_Toc47164642"></a><a name="_Toc33784664"></a>Definitions:</h3>
<h4><a name="_Toc47164643"></a>Definition of get_table()</h4>
<p><em>def </em>get_table(url='http://www.lvceli.lv/cms/'):<br /> &nbsp;&nbsp;&nbsp; <em>with </em>requests.session() <em>as </em>s:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; r = s.post(url, data=login_data, headers=headers)<br /> <br /> &nbsp;&nbsp;&nbsp; soup = BeautifulSoup(r.content, 'html5lib')<br /> &nbsp;&nbsp;&nbsp; <em>return </em>soup.find("table", attrs={"class": "norm", "id": "table-1"})</p>
<p>&nbsp;</p>
<p>In this method, making a POST request to a website with data that contains login and password to get access to the table with observations. Because every successful application returns a whole webpage to separate our table from the whole piece of HTML to get by using unique attributes of the table that are needed. In details:</p>
<p>soup &ndash; an instance of <strong>class BeautifulSoup</strong>, where HTML will be stored.</p>
<p>Using method <em>find(), </em>and in arguments, passing the tag that looks for, and it&rsquo;s unique attributes to be sure that a correct table in the result is taken.</p>
<h4><a name="_Toc47164644"></a>Definition of get_data_lists_from_table()</h4>
<p><em>def </em>get_data_lists_from_table(table) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; tmp_list = []<br /> &nbsp;&nbsp;&nbsp; data_list = []<br /> <br /> &nbsp;&nbsp;&nbsp; <em>for </em>row <em>in </em>table.find_all('tr'):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>for </em>cell <em>in </em>row.find_all('td'):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; tmp_list.append(cell.text)<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>while </em><em>len</em>(tmp_list) &lt; 19:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; tmp_list.append('-')<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_list.append(tmp_list)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; tmp_list = []<br /> <br /> &nbsp;&nbsp;&nbsp; data_list.pop(0)<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>data_list</p>
<p>&nbsp;</p>
<p>In this method, iterating through every row in the table and through every cell of row (loop in loop, internal circuit) and taking text from HTML tags and adding it to the temporal list, which appends to the main index of data. At the end of the method, the first list of data is being deleted because it contains only titles of columns that is not needed in our main list.</p>
<h1><a name="_Toc47164645"></a><a name="_Toc33784665"></a>3.&nbsp;&nbsp;&nbsp; MySQL Connection</h1>
<p>To be able to get data from the MySQL database, <strong>MySQLClient.py,</strong> which has few methods to download data from a table in the database, and it uses <strong>mysql.connector</strong> module for Python to get a possibility to connect to the database.</p>
<p>A simple instruction to start:</p>
<ol>
<li>Firstly, it is needed to create a client:</li>
</ol>
<p>&nbsp;</p>
<p>sql_client = MySQLClient('xx.xx.xx.xx', 'xxx', 'xxx', 'xxx')</p>
<p>&nbsp;</p>
<p>In parameters, we pass the IP address of database, login, and password to get access and name of the table to get data from. In this case, it is a database with observations for one month.</p>
<ol start="2">
<li>Now it is connected to the database and have two ways: get all of the data stored in the database or data from exact station/s. It can be either use <em>get_all_info_from_database</em>() or <em>get_info_by_station()/get_info_by_stations(). </em>The difference is in the amount of returned data and which data is needed.<em><br /> </em>Example:</li>
</ol>
<p>records = sql_client.get_info_by_station('LV01')</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Now in variable <em>records</em> is stored all of observations from station with code &ldquo;LV01&rdquo;.</p>
<p>records = sql_client.get_all_info_from_database()</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; But using method to get all of stored observations, it will get all of them and store &nbsp;&nbsp; in &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; variable <em>records.</em></p>
<p>records = sql_client.get_info_by_stations(['LV01', 'LV02', 'LV03'])</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; By using this method it can pass list of station codes and return lists of data for every &nbsp; station that is asked.</p>
<h3><a name="_Toc47164646"></a><a name="_Toc33784666"></a>Definitions</h3>
<h4><a name="_Toc47164647"></a>Definition of MySQLClient __init__() also known as class constructor</h4>
<p><em>def </em><em>__init__</em>(<em>self</em>, host, username, password, database):<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.host = host<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.username = username<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.password = password<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.database = database<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.database_connection = <em>self</em>.connect_to_database()<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.cursor = <em>self</em>.database_connection.cursor()</p>
<p>Here is just create an instance of the class with all the needed variables. <em>self.cursor</em> is a variable that is responsible for interaction with the database: making queries, executing commands, and returning results.</p>
<h4><a name="_Toc47164648"></a>Definition of MySQLClient connect_to_database()</h4>
<p><em>def </em>connect_to_database(<em>self</em>):<br /> &nbsp;&nbsp;&nbsp; database_connection = mysql.connector.connect(<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; host=<em>self</em>.host,<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; user=<em>self</em>.username,<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; passwd=<em>self</em>.password,<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; database=<em>self</em>.database<br /> &nbsp;&nbsp;&nbsp; )<br /> &nbsp;&nbsp;&nbsp; <em>return </em>database_connection</p>
<p>In this method, an establishing the connection to the database using data provided to <em>__init__()</em> and method of <strong>mysql.connector</strong> and returning it to variable in <em>__init__().</em></p>
<h4><a name="_Toc47164649"></a>Definition of get_all_info_from_database()</h4>
<p><em>def </em>get_all_info_from_database(<em>self</em>):<br /> &nbsp;&nbsp;&nbsp; command = 'SELECT * FROM data_records'<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.cursor.execute(command)<br /> &nbsp;&nbsp;&nbsp; records = <em>self</em>.cursor.fetchall()<br /> &nbsp;&nbsp;&nbsp; <em>return </em>records</p>
<p>In this method, an executing simple query written and stored in variable <em>command</em> and returning all observations from the database.</p>
<h4><a name="_Toc47164650"></a>Definition of get_info_by_station()</h4>
<p><em>def </em>get_info_by_station(<em>self</em>, station_code: <em>str </em>= 'LV01'):<br /> &nbsp;&nbsp;&nbsp; command = 'SELECT * FROM data_records WHERE stacijas_kods = %s'<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.cursor.execute(command, (station_code,))<br /> &nbsp;&nbsp;&nbsp; records = <em>self</em>.cursor.fetchall()<br /> &nbsp;&nbsp;&nbsp; <em>return </em>records</p>
<p>In this method, an executing the query to the database and returning all rows in the database with data from the station passed in parameters or defined as the default parameter. In variable <em>command, the </em>SQL command is constructed to make a proper query.</p>
<h4><a name="_Toc47164651"></a>Definition of get_info_by_stations()</h4>
<p><em>def </em>get_info_by_stations(<em>self</em>, station_codes: <em>list</em>) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; info = []<br /> &nbsp;&nbsp;&nbsp; <em>for </em>station_code <em>in </em>station_codes:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; command = 'SELECT * FROM data_records WHERE stacijas_kods = %s'<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>self</em>.cursor.execute(command, (station_code,))<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; records = <em>self</em>.cursor.fetchall()<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; info.append(records)<br /> &nbsp;&nbsp;&nbsp; <em>else</em>:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>info</p>
<p>This method does almost everything the same as the previous one; however, for many stations and returns, a list of records from many stations.</p>
<h1><a name="_Toc47164652"></a><a name="_Toc33784667"></a>4.&nbsp;&nbsp;&nbsp; MongoDB Connection</h1>
<h2><a name="_Toc47164653"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; I.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Difference between database clients</h2>
<p>Comparing with the MySQL module, the program has methods both for importing and exporting data if a user with a login/password that is passed to <em>MongoDBClient</em> has permission to do so.</p>
<p>This program is capable of working with MongoDB as well. Methods are located in <strong>MongoDBClient.py</strong> and <strong>AutoDBFiller.py</strong><em>. </em>They use <strong>pymongo</strong> module to connect to the MongoDB cluster, where databases with collections of data are stored.</p>
<p>A simple instruction to start:</p>
<ol>
<li>In the case with MySQL, first of all, is creating a client that will connect to the cluster:</li>
</ol>
<p>mongo_db_client = MongoDBClient('login', 'password', 'MeteoInfoTable', 'LastInsertTable')</p>
<p>In arguments, passing login and password to connect to the cluster, name of the database where observations are stored, and name of the database where the time of the last insert is stored.</p>
<h3><a name="_Toc47164654"></a><a name="_Toc33784668"></a>Definitions</h3>
<h4><a name="_Toc47164655"></a>Definition of MongoDBClient __init__() also known as class constructor</h4>
<p><em>def </em><em>__init__</em>(<em>self</em>, login: <em>str</em>, password: <em>str</em>, main_database_name: <em>str</em>, time_database_name: <em>str</em>):<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.my_client = <em>self</em>.get_connection(login, password)<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.main_database_name = main_database_name<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.__main_database = <em>self</em>.my_client[<em>self</em>.main_database_name]<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.time_database_name = time_database_name<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.__time_database = <em>self</em>.my_client[<em>self</em>.time_database_name]<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.is_it_first_filling = <em>self</em>.is_not_first_filling_made()</p>
<p>In this method, creating our client by establishing a connection and defining essential variables.</p>
<h4><a name="_Toc47164656"></a>Definition of get_connection()</h4>
<p><em>def </em>get_connection(login, password):<br /> &nbsp;&nbsp;&nbsp; <em>return </em>pymongo.MongoClient(<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "mongodb+srv://xxxxx".format(login, password))</p>
<p>In this method an establishing connection using login and password provided to <em>__init__() </em>and returning it to class constructor.</p>
<h2><a name="_Toc47164657"></a><a name="_Toc33784669"></a>&nbsp;&nbsp;&nbsp; II.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; MongoDB Importing</h2>
<p>1.&nbsp; records = mongo_db_client.get_all_info_from_main_database()</p>
<p>Now it is stored all information from main database in list of lists with dictionaries inside. Consider this as two-dimension array of dictionaries like [[{}, {}, {}], [{}, {}, {}]]</p>
<p>&nbsp;</p>
<p>2.&nbsp; records = mongo_db_client.get_data_from_collection('A1 km 12 Ādaži')</p>
<p>If needed to get info from one station, it is possible to use this method and pass the name of the station.</p>
<p>&nbsp;</p>
<p>3.&nbsp; records = mongo_db_client.get_data_from_collections(['A1 km 12 Ādaži', 'A1 km 21 Lilaste'])</p>
<p>In case needed observations from many stations it is possible to use this method and pass list of station names.</p>
<ol start="4">
<li>Please, be attentive that in the case of MySQL database, station codes were used but with MongoDB names of stations!</li>
<li>How to process this data correctly and use it in estimations is described later.</li>
</ol>
<h3><a name="_Toc47164658"></a><a name="_Toc33784670"></a>Definitions</h3>
<h4><a name="_Toc47164659"></a>Definition of get_all_info_from_main_database()</h4>
<p><em>def </em>get_all_info_from_main_database(<em>self</em>) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; collection_names = <em>self</em>.__main_database.list_collection_names()<br /> &nbsp;&nbsp;&nbsp; list_of_info = []<br /> &nbsp;&nbsp; &nbsp;temp_list = []<br /> &nbsp;&nbsp;&nbsp; <em>for </em>name <em>in </em>collection_names:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>for </em>search_result <em>in </em><em>self</em>.__main_database[name].find():<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; search_result.pop('_id')<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; search_result['Station'] = name<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; temp_list.append(search_result)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_info.append(temp_list)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; temp_list = []<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>list_of_info</p>
<p>In this method, calling for all collections present in the main database, and depending on names returned in list requests are being made in the loop. In <em>for</em> loop, we are deleting <em>_id </em>keyword with the value from every returned result because it&rsquo;s unnecessary and adding <em>Station </em>keyword with a value of the name of collection getting at this moment, so every result has the name of the station it relates to. As a result, getting a list of lists of dictionaries as it was described earlier.</p>
<h4><a name="_Toc47164660"></a>Definition of get_data_from_collection()</h4>
<p><em>def </em>get_data_from_collection(<em>self</em>, station_name: <em>str</em>) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; list_of_info = []<br /> &nbsp;&nbsp;&nbsp; <em>for </em>search_result <em>in </em><em>self</em>.__main_database[station_name].find():<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; search_result.pop('_id')<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; search_result['Station'] = station_name<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_info.append(search_result)<br /> &nbsp;&nbsp;&nbsp; <em>else</em>:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>list_of_info</p>
<p>In this method, passing the name of one station as a parameter and making a request to database, processing results of search the same as in previous method and returning list of info.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h4><a name="_Toc47164661"></a>Definition of get_data_from_collections()</h4>
<p><em>def </em>get_data_from_collections(<em>self</em>, station_names: <em>list</em>) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; list_of_info = []<br /> <br /> &nbsp;&nbsp;&nbsp; <em>for </em>station_name <em>in </em>station_names:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>for </em>search_result <em>in </em><em>self</em>.__main_database[station_name].find():<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; search_result.pop('_id')<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; search_result['Station'] = station_name<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_info.append(search_result)<br /> &nbsp;&nbsp;&nbsp; <em>else</em>:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>list_of_info</p>
<p>In this method, passing the list of station names, but the logic is the same as in two previous methods. The only difference is that it iterates through, the given list of names, that contain those names which the user-provided.</p>
<h2><a name="_Toc47164662"></a><a name="_Toc33784671"></a>&nbsp;III.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; MongoDB Exporting</h2>
<ol>
<li>To use all of functionality it should recreate client and use AutoDBFiller()</li>
</ol>
<p>mongo_db_client = AutoDBFiller('login', 'password', 'MeteoInfoTable', 'LastInsertTable')</p>
<p>Parameters are the same as in case with MongoDBClient() because <strong><em>class AutoDBFiller</em></strong> is child-class of <strong><em>class</em></strong><em> <strong>MongoDBClient</strong> </em>and has all of it methods and some new.</p>
<ol start="2">
<li>As described earlier, it is possible to use requests to take data from the website, but this data has to be processed before it can be exported to the database, so be sure to check the Data Handling chapter and methods presented there.</li>
</ol>
<h1><a name="_Toc47164663"></a><a name="_Toc33784672"></a>5.&nbsp;&nbsp;&nbsp; Data Handling</h1>
<p>Created <strong>DataHandler.py </strong>with methods to process data in different ways to prepare it for different usage. This chapter will be seprated in many small to systemize data and increase the readability of the document.</p>
<h2><a name="_Toc47164664"></a><a name="_Toc33784673"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; I.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; For exporting to MongoDB</h2>
<p>After getting the list of lists of values from the website, need to turn it into a JSON-like document to be able to export it to MongoDB because this database contains all records in JSON. Python is a data type called the <em>dictionary, </em>so a set of methods that will help to prepare all the data to export.</p>
<p>data_dicts = DataHandler.get_data_dicts(data_lists)</p>
<p>Here useing variable <em>data_lists </em>from the Website Connection chapter, which contains a list of lists of values from the website. After calling this method, turning a list of lists into a list of dictionaries like [{}, {}, {}]</p>
<p>Now data can be exported to the database. This process will be described in the MongoDB Exporting chapter.</p>
<h3><a name="_Toc47164665"></a><a name="_Toc33784674"></a>Definitions</h3>
<h4><a name="_Toc47164666"></a>Definition of get_data_dicts()</h4>
<p><em>def </em>get_data_dicts(data_lists) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; data_dicts = []<br /> <br /> &nbsp;&nbsp;&nbsp; <em>for </em>data <em>in </em>data_lists:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_dict = {'Station': data[0],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Time': data[1],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Date': DataHandler.get_date(),<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Air Temperature': data[2],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Air Temperature(-1 h)': data[3],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Humidity': data[4],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Dew Point': data[5],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Precipitation': data[6],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Intensity': data[7],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Visibility': data[8],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Road Temperature': data[9],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Road Temperature(-1 h)': data[10],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Road Condition': data[11],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Road Warning': data[12],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Freezing Point': data[13],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Road Temperature 2': data[14],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Road Temperature 2(-1 h)': data[15],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Road Condition 2': data[16],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Road Warning 2': data[17],<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'Freezing Point 2': data[18]}<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_dicts.append(data_dict)<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>data_dicts</p>
<p>This method iterates through a list of data, takes values from the list by indexes they are stored, and append created dictionary to list which will be returned in the result.</p>
<h4><a name="_Toc47164667"></a>Definition of get_date()</h4>
<p><em>def </em>get_date() -&gt; <em>str</em>:<br /> &nbsp;&nbsp;&nbsp; <em>from </em>datetime <em>import </em>datetime<br /> <br /> &nbsp;&nbsp;&nbsp; year = datetime.now().year<br /> &nbsp;&nbsp;&nbsp; month = datetime.now().month<br /> &nbsp;&nbsp;&nbsp; day = datetime.now().day<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>'Year: {} Month: {} Day: {}'.format(year, month, day)</p>
<p>This method takes current date-time, adds its parts to string (year, month, and day), and returns this string. It uses <strong>datetime </strong>module to obtain the current date and time.</p>
<h2><a name="_Toc47164668"></a><a name="_Toc33784675"></a>&nbsp;&nbsp;&nbsp; II.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Process data from MongoDB</h2>
<h3><a name="_Toc47164669"></a><a name="_Toc33784676"></a>Data from MongoDB database</h3>
<p>lists_of_measurements, list_of_station_names = DataHandler.get_prepared_lists_for_estimation(main_data, 'Dew Point')</p>
<p>Called method returns two lists: with measurements (observations) and with station names whose data returned. Because of the chance that sometimes stations haven&rsquo;t been gathering data program checks every list and, if it is possible to fill missing data, it fills, if not &ndash; deletes the list of data. Station names aren&rsquo;t needed for estimation but are essential for building plots. Plots are described later.</p>
<h3><a name="_Toc47164670"></a><a name="_Toc33784677"></a>Definitions</h3>
<h4><a name="_Toc47164671"></a>Definition of get_prepared_lists_for_estimation()</h4>
<p><em>def </em>get_prepared_lists_for_estimation(main_data, value: <em>str </em>= 'Dew Point') -&gt; <em>tuple</em>:<br /> &nbsp;&nbsp;&nbsp; lists_of_chosen_values = DataHandler.get_lists_of_chosen_values_with_station_names(main_data, value)<br /> <br /> &nbsp;&nbsp;&nbsp; lists_of_measurements_with_station_names = DataHandler.get_lists_of_measurements_with_station_names(<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; lists_of_chosen_values)<br /> <br /> &nbsp;&nbsp;&nbsp; list_of_station_names = DataHandler.get_station_names(lists_of_measurements_with_station_names)<br /> <br /> &nbsp;&nbsp;&nbsp; lists_of_measurements_without_station_names = DataHandler.get_lists_of_measurements_without_station_names(<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; lists_of_measurements_with_station_names)<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>lists_of_measurements_without_station_names, list_of_station_names</p>
<p>This method does a lot, but basically, it does what it has to. Here are four steps:</p>
<ol>
<li>Getting a list of lists of chosen values or values defined as a default parameter, and at the end of every list, appending the name of the station to which it is related. For this goal is used <em>get_lists_of_chosen_values_with_station_names().</em></li>
<li>Because all values are stored as text(string type), to convert it to numbers to be able to work with data. For this goal is used <em>get_lists_of_measurements_with_station_names()</em></li>
</ol>
<p>In this method are being checked lists of data is it possible to fill missing data and if it is possible, it is being filled. As a result, suitable lists returned. Those ones who weren&rsquo;t fillable were deleted.</p>
<ol start="3">
<li>Now the program starts dividing the list of data to two lists: list of station names and list_of_measurements. For first goal is used <em>get_station_names().</em></li>
<li><em>For </em>last step is used <em>get_list_of_measurements_without_station_names().</em></li>
</ol>
<h4><a name="_Toc47164672"></a>Definition of get_lists_of_chosen_values_with_station_names()</h4>
<p><em>def </em>get_lists_of_chosen_values_with_station_names(lists_of_dicts: <em>list</em>, value_name: <em>str</em>) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; list_of_values = []<br /> &nbsp;&nbsp;&nbsp; temp_list = []<br /> <br /> &nbsp;&nbsp;&nbsp; <em>for </em>list_of_dicts <em>in </em>lists_of_dicts:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>for </em>data_dict <em>in </em>list_of_dicts:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; temp_list.append(data_dict[value_name])<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>else</em>:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; temp_list.append(data_dict['Station'])<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_values.append(temp_list)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; temp_list = []<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>list_of_values</p>
<p>Here is a simple method that fills the list with lists of values that are being passed as argument and station names values belong to.</p>
<h4><a name="_Toc47164673"></a>Definition of get_lists_of_measurements_with_station_names()</h4>
<p><em>def </em>get_lists_of_measurements_with_station_names(lists_of_values: <em>list</em>) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; lists_of_measurements = []<br /> <br /> &nbsp;&nbsp;&nbsp; <em>for </em>list_of_values <em>in </em>lists_of_values:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>if </em>'-' <em>in </em>list_of_values <em>or </em>'' <em>in </em>list_of_values:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_values.pop()<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>if </em>DataHandler.is_possible_to_fill_missing_data(list_of_values):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; indexes = DataHandler.get_indexes_for_filling(list_of_values)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_values = DataHandler.fill_missing_data(list_of_values, indexes)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>else</em>:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>continue<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </em>lists_of_measurements.append(DataHandler.get_list_of_float_numbers_and_station(list_of_values))<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>lists_of_measurements</p>
<p>This method iterates through lists of values, and if there are &lsquo;-&lsquo; or empty spots, these lists are sent to the special method to be checked if it is possible to fill missing data, and if it is, missing data will be filled. If it is not possible, these lists will not be added to the final list of data and then deleted from memory. Before appending list of values to main lists all values are turned to <em>float </em>type in <em>get_list_of_float_numbers_and_station().</em></p>
<h4><a name="_Toc47164674"></a>Definition of is_possible_to_fill_missing_data()</h4>
<p><em>def </em>is_possible_to_fill_missing_data(list_of_values: <em>list</em>) -&gt; <em>bool</em>:<br /> &nbsp;&nbsp;&nbsp; index = 0<br /> &nbsp;&nbsp;&nbsp; adder = 1<br /> <br /> &nbsp;&nbsp;&nbsp; <em>while </em>adder &lt; 5 <em>and </em>index &lt; <em>len</em>(list_of_values) - 1 <em>and </em>index + adder &lt; <em>len</em>(list_of_values):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>if </em>list_of_values[index] == '-' <em>and </em>list_of_values[index + adder] == '-':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; adder += 1<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>else</em>:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; index += adder<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; adder = 1<br /> &nbsp;&nbsp;&nbsp; <em>else</em>:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>if </em>'' <em>in </em>list_of_values:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return False<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if </em>adder &gt; 4:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return False<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; elif </em>1 &lt; adder &lt; 5 <em>and </em>adder == <em>len</em>(list_of_values):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return False<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else</em>:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return True</em></p>
<p>This method simply counts the quantity of missing data in a row, and if there is somewhere in the list, five and more missing data samples method returns <em>False</em>. It will return <em>False </em>also if there is just empty string because that means that all list is empty(a feature of the website).</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h4><a name="_Toc47164675"></a>Definition of get_indexes_for_filling()</h4>
<p><em>def </em>get_indexes_for_filling(list_of_values: <em>list</em>) -&gt; <em>tuple</em>:<br /> <br /> &nbsp;&nbsp;&nbsp; index = 0<br /> &nbsp;&nbsp;&nbsp; adder = 1<br /> <br /> &nbsp;&nbsp;&nbsp; indexes = []<br /> <br /> &nbsp;&nbsp;&nbsp; <em>while </em>adder &lt; 5 <em>and </em>index &lt; <em>len</em>(list_of_values) - 1 <em>and </em>index + adder &lt; <em>len</em>(list_of_values):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>if </em>adder == 1 <em>and </em>list_of_values[index] == '-' <em>and </em>list_of_values[index + 1] != '-':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; indexes.append([index, 'one'])<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>if </em>list_of_values[index] == '-' <em>and </em>list_of_values[index + adder] == '-':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; adder += 1<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>elif </em>adder != 1:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; indexes.append([index - 1, index + adder, 'normal'])<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; index += adder<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; adder = 1<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>else</em>:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; index += adder<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; adder = 1<br /> &nbsp;&nbsp;&nbsp; <em>else</em>:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>if </em>adder != 1:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; indexes.append([index - 1, index + adder, 'in the end'])</p>
<p>This method searches for all spots in the list and creates a list of coordinates for another method to fill missing data later correctly. There are three types of cords: usual series of missing spots, when only one spot missing data(in real life there is very little chance that this situation will occur, but I left this variant just in case) and when series of missing spots are located at the end of the list. How these scenarios are processed is shown in the next method definition.</p>
<h4><a name="_Toc47164676"></a>Definition of fill_missing_data_in_list()</h4>
<p><em>def </em>fill_missing_data_in_list(list_of_values: <em>list</em>, indexes: <em>tuple</em>) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; <em>for </em>index_list <em>in </em>indexes:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>if </em>index_list[-1] == 'normal':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; average = (list_of_values[index_list[0]] + list_of_values[index_list[1]]) / 2<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>for </em>i <em>in </em><em>range</em>(index_list[0] + 1, index_list[1]):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_values[i] = average<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>elif </em>index_list[-1] == 'one':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; average = (list_of_values[index_list[0] - 1] + list_of_values[index_list[0] + 1]) / 2<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_values[index_list[0]] = average<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>elif </em>index_list[-1] == 'in the end':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>for </em>i <em>in </em><em>range</em>(index_list[0], index_list[1]):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_values[i] = list_of_values[index_list[0]]<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>list_of_values</p>
<p>This method returns the list with filled missing spots. It iterates through a list of coordinates for filling and depending on coordinates and type of variant of the positioning of missing spots filling occurs.</p>
<h4><a name="_Toc47164677"></a>Definition of get_list_of_float_numbers_and_station()</h4>
<p><em>def </em>get_list_of_float_numbers_and_station(list_of_values: <em>list</em>) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; list_of_data = []<br /> <br /> &nbsp;&nbsp;&nbsp; <em>for </em>value <em>in </em>list_of_values:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>try</em>:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_data.append(<em>float</em>(value))<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>except </em><em>ValueError</em>:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_data.append(value)<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>list_of_data</p>
<p>The simple method to turn every value in the list from <em>str </em>to <em>float </em>except station name. The method returns a new list of data.</p>
<h4><a name="_Toc47164678"></a>Definition of get_station_names()</h4>
<p><em>def </em>get_station_names(list_of_lists_of_data: <em>list</em>) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; list_of_station_names = []<br /> <br /> &nbsp;&nbsp;&nbsp; <em>for </em>list_of_data <em>in </em>list_of_lists_of_data:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_station_names.append(list_of_data[-1])<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>list_of_station_names</p>
<p>A simple method that just takes the last element from every list which is station name and appends it to list of station names.</p>
<h4><a name="_Toc47164679"></a>Definition of get_lists_of_measurements_without_station_names()</h4>
<p><em>def </em>get_lists_of_measurements_without_station_names(<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_lists_of_measurements_with_station_names: <em>list</em>) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; list_of_lists_of_measurements_without_station_names = []<br /> <br /> &nbsp;&nbsp;&nbsp; <em>for </em>list_of_measurements <em>in </em>list_of_lists_of_measurements_with_station_names:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_measurements.pop(<em>len</em>(list_of_measurements) - 1)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_lists_of_measurements_without_station_names.append(list_of_measurements)<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>list_of_lists_of_measurements_without_station_names</p>
<p>A simple method that iterates through every list deletes the last element of every list, which is station name and append these lists to the final list that will be returned.</p>
<h2><a name="_Toc47164680"></a><a name="_Toc33784678"></a>&nbsp;III.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Process data from MySQL</h2>
<p>index = DataHandler.get_index_of_value('Dew Point')</p>
<p>If needed to estimate data from MySQL database first needs to be done is get index of value that are needed to make estimation with.</p>
<p>list_of_measurements = DataHandler.get_exact_value_from_my_sql_records(records, index)</p>
<p>Now after getting exact value from records returned from MySQL database.</p>
<p>IMPORTANT NOTE!</p>
<p>records = sql_client.get_info_by_stations(['LV01', 'LV02', 'LV03'])<br /> index = DataHandler.get_index_of_value('Dew Point')<br /> lists_of_measurements = DataHandler.get_exact_value_from_many_my_sql_records(records, index)</p>
<p>If needed to get values from some exact stations than should use other method to extract value because previous method is only for processing one station.</p>
<p>lists_of_measurements = DataHandler.get_lists_of_floats(lists_of_measurements)<br /> list_of_measurements = DataHandler.get_list_of_floats(list_of_measurements)</p>
<p>Depending on situation it should be using method for process info from one station or from many stations.</p>
<p>At this moment, it should have a list of values or lists of values. However, in this list/lists may be missing values of type <em>None.</em> A simple method to replace them with a dash of type <em>str, </em>so these lists could be suitable for usage with methods for filling missing data I described earlier.</p>
<p>lists_of_measurements = DataHandler.replace_none_with_dash(lists_of_measurements)</p>
<p>This method accepts a list of lists and returns it after processing.</p>
<p>Now passing lists for filling missing data if it is possible.</p>
<p>lists_of_measurements = DataHandler.fill_missing_data_in_lists(lists_of_measurements)</p>
<p>This method accepts a list of lists as well and returns it. Some details of functionality will be described in the next Definition chapter.</p>
<p>However, in lists that returned are present elements that can&rsquo;t be used in estimation due to not every list, missing data were filled.</p>
<p>Now the only option is to check which lists contain <em>str </em>elements, dashes put instead of <em>None, </em>or empty at all and remove them from the main list of measurements. Besides, station codes should be updated because our data needs to be related to the correct station.</p>
<p>station_codes = DataHandler.get_station_codes()</p>
<p>The first step &ndash; just create a list of station codes using this simple method.</p>
<p>station_codes, lists_of_measurements = DataHandler.zip_codes_and_measurements(station_codes, lists_of_measurements)</p>
<p>Now passing our lists in the following method, and it will return corrected lists that can be used in estimation and plot building.</p>
<p>After these manipulations, data is ready for estimation. The process of evaluation is described later.</p>
<h3><a name="_Toc47164681"></a><a name="_Toc33784679"></a>Definitions</h3>
<h4><a name="_Toc47164682"></a>Definition of get_index_of_value()</h4>
<p><em>def </em>get_index_of_value(value: <em>str </em>= 'Dew Point') -&gt; <em>int</em>:<br /> &nbsp;&nbsp;&nbsp; <em>if </em>value == 'id':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>0<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Station code':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>1<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Datetime':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>2<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Air Temperature':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>3<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Air Temperature(-1 h)':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>4<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Humidity':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>5<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Dew Point':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>6<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Precipitation':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>7<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Intensity':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>8<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Visibility':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>9<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Road Temperature':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>10<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Road Temperature(-1 h)':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>11<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Road Condition':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>12<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Road Warning':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>13<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Freezing Point':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>14<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Road Temperature 2':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>15<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Road Temperature 2(-1 h)':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>16<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Road Condition 2':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>17<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Road Warning 2':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>18<br /> &nbsp;&nbsp;&nbsp; <em>elif </em>value == 'Freezing Point 2':<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>return </em>19</p>
<p>A simple method that returns <em>int </em>as an index of value passed in argument or which is defined as a default parameter.</p>
<h4><a name="_Toc47164683"></a>Definition of get_exact_value_from_my_sql_records()</h4>
<p><em>def </em>get_exact_value_from_my_sql_records(records: <em>tuple</em>, index: <em>int</em>) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; values = []<br /> <br /> &nbsp;&nbsp;&nbsp; <em>for </em>record <em>in </em>records:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; values.append(record[index])<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>values</p>
<p>A simple method that just iterates through records and takes elements by index and adds them in a list that will be returned in the end.</p>
<h4><a name="_Toc47164684"></a>Definition of get_exact_value_from_many_my_sql_records()</h4>
<p><em>def </em>get_exact_value_from_many_my_sql_records(list_of_records: <em>list</em>, index: <em>int</em>) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; values = []<br /> <br /> &nbsp;&nbsp;&nbsp; <em>for </em>records <em>in </em>list_of_records:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; values.append(DataHandler.get_exact_value_from_my_sql_records(records, index))<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>values</p>
<p>This method does the same as the previous one but for records from many stations. Returns list of lists.</p>
<h4><a name="_Toc47164685"></a>Definition of replace_none_with_dash()</h4>
<p><em>def </em>replace_none_with_dash(lists_of_measurements: <em>list</em>) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; i = 0<br /> <br /> &nbsp;&nbsp;&nbsp; <em>for </em>list_of_measurements <em>in </em>lists_of_measurements:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>for </em>_ <em>in </em>list_of_measurements:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>if </em>list_of_measurements[i] <em>is None</em>:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_measurements[i] = '-'<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i += 1<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i = 0<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>lists_of_measurements</p>
<p>This simple method just iterates through every element of every row and, if it is <em>None </em>type, replaces it on &lsquo;-&lsquo; character.</p>
<h4><a name="_Toc47164686"></a>Definition of fill_missing_data_in_lists()</h4>
<p><em>def </em>fill_missing_data_in_lists(lists_of_measurements: <em>list</em>) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; i = 0<br /> &nbsp;&nbsp;&nbsp; <em>for </em>list_of_measurement <em>in </em>lists_of_measurements:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>if </em>DataHandler.is_possible_to_fill_missing_data(list_of_measurement):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; indexes = DataHandler.get_indexes_for_filling(list_of_measurement)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_measurement = DataHandler.fill_missing_data_in_list(list_of_measurement, indexes)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; lists_of_measurements[i] = list_of_measurement<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i += 1<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>else</em>:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i += 1<br /> &nbsp;&nbsp;&nbsp; <em>return </em>lists_of_measurements</p>
<p>This method iterates through every list and checks if it is possible to fill missing data or not and if it is, it makes filling using already described methods.</p>
<p>IMPORTANT NOTE!</p>
<p>This method works with the whole list at a time, so if even there are only one series of missing data that couldn&rsquo;t be filled, the entire list will be ignored.</p>
<h4><a name="_Toc47164687"></a>Definition of get_station_codes()</h4>
<p><em>def </em>get_station_codes() -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; station_codes = []<br /> <br /> &nbsp;&nbsp;&nbsp; <em>for </em>i <em>in </em><em>range</em>(1, 65):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; station_code = 'LV{:02d}'.format(i)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; station_codes.append(station_code)<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>station_codes</p>
<p>This method simply creates a list, fills it with station codes in <em>str </em>type, and returns it in the result.</p>
<h4><a name="_Toc47164688"></a>Definition of zip_codes_and_measurements()</h4>
<p><em>def </em>zip_codes_and_measurements(station_codes: <em>list</em>, lists_of_measurements: <em>list</em>) -&gt; <em>tuple</em>:<br /> &nbsp;&nbsp;&nbsp; stop = <em>len</em>(lists_of_measurements)<br /> &nbsp;&nbsp;&nbsp; i = 0<br /> <br /> &nbsp;&nbsp;&nbsp; <em>while </em>i &lt; stop:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>if </em>'-' <em>in </em>lists_of_measurements[i] <em>or not </em><em>bool</em>(lists_of_measurements[i]):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; lists_of_measurements.pop(i)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; station_codes.pop(i)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; stop -= 1<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i = 0<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>else</em>:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i += 1<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>station_codes, lists_of_measurements</p>
<p>This method checks every list is it containing dashes or is empty, and if it is, then it deletes this list from the main list and corresponding station code from the list of station codes. As a result, modified lists are returned.</p>
<h2><a name="_Toc47164689"></a><a name="_Toc33784680"></a>&nbsp; IV.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Accuracy</h2>
<p>This chapter will be useful after getting familiar with the Estimation chapter because skill is counted using measurements and estimates. Anyway, the calculation of efficiency is handled by <strong>DataHandler.py, </strong>so this process will be described here.</p>
<p>Few steps should be made to calculate accuracy:</p>
<ol>
<li>Cast all data values to <em>int </em>type</li>
</ol>
<p>lists_of_estimates = DataHandler.get_lists_of_ints(lists_of_estimates)<br /> lists_of_measurements = DataHandler.get_lists_of_ints(lists_of_measurements)</p>
<ol start="2">
<li>Use method, pass lists with data as argument and will get list of accuracies</li>
</ol>
<p>accuracies = DataHandler.get_accuracies(lists_of_measurements, lists_of_estimates)</p>
<p>Now having list of accuracies of stations that were used in estimation processs.</p>
<h3><a name="_Toc47164690"></a><a name="_Toc33784681"></a>Definitions</h3>
<h4><a name="_Toc47164691"></a>Definition of get_lists_of_ints()</h4>
<p><em>def </em>get_lists_of_ints(lists_of_values) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; <em>for </em>values <em>in </em>lists_of_values:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i = 0<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>while </em>i &lt; <em>len</em>(values):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; values[i] = <em>int</em>(values[i])<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i += 1<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>lists_of_values</p>
<p>This method iterates through every element of every list and casts it to <em>int</em>.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h4><a name="_Toc47164692"></a>Definition of get_accuracies()</h4>
<p><em>def </em>get_accuracies(lists_of_measurements: <em>list</em>, lists_of_estimates: <em>list</em>) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; accuracies = []<br /> &nbsp;&nbsp;&nbsp; <em>for </em>measurements, estimates <em>in </em><em>zip</em>(lists_of_measurements, lists_of_estimates):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; accuracies.append(DataHandler.get_accuracy(measurements, estimates))<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>accuracies</p>
<p>This method iterates through every list of measurements, estimates, and appends the result of <em>get_accuracy() </em>method, which is described below.</p>
<h4><a name="_Toc47164693"></a>Definition of get_accuracy()</h4>
<p><em>def </em>get_accuracy(measurements: <em>list</em>, estimates: <em>list</em>) -&gt; <em>float</em>:<br /> &nbsp;&nbsp;&nbsp; <em>from </em>sklearn.metrics <em>import </em>accuracy_score<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>accuracy_score(measurements, estimates)</p>
<p>This method uses a method from <strong>sklearn </strong>module to calculate accuracy and returns the result.</p>
<h1><a name="_Toc47164694"></a><a name="_Toc33784682"></a>6.&nbsp;&nbsp;&nbsp; Estimation</h1>
<p>For estimation purposes, <strong>KalmanFilter.py </strong>is created that has a basic implementation of the Kalman Filter for a one-dimension model.</p>
<p>kalman_filter = KalmanFilter(error_in_estimate, initial_estimate, error_in_estimate, measurements)</p>
<p>The first step is to create Kalman filter object and pass needed arguments: error in the estimate, an initial estimate, error in the estimate, and list of measurements that will be used in the estimation process.</p>
<p>estimates = kalman_filter.get_estimates()</p>
<p>Now it can get a list of estimates by using only one method.</p>
<p>However, if working with a list of lists, then can use the static method from <strong>KalmanFilter.py </strong>that will handle essential processes and return us a list of lists of estimates.</p>
<p>lists_of_estimates = KalmanFilter.get_lists_of_estimates(lists_of_measurements, error_in_estimate, error_in_measurement)</p>
<p>In arguments, passing lists of measurements, errors in the estimate, and error in measurement. As a result, getting our estimations that can be used for building plots. Plots are described later.</p>
<h3><a name="_Toc47164695"></a><a name="_Toc33784683"></a>Definitions</h3>
<h4><a name="_Toc47164696"></a>Definition of KalmanFilter __init__() also known as class constructor</h4>
<p><em>def </em><em>__init__</em>(<em>self</em>, initial_error_in_estimate, __initial_estimate, __error_in_measurement, __measurements):<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.__measurements = __measurements<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.__estimate = __initial_estimate<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.__error_in_estimate = initial_error_in_estimate<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.__error_in_measurement = __error_in_measurement<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.__measurement = <em>None<br /> &nbsp;&nbsp;&nbsp; </em><em>self</em>.__kalman_gain = <em>None</em></p>
<p>In this method, is just declare essential variables for the estimation process.</p>
<h4><a name="_Toc47164697"></a>Definition of get_estimates()</h4>
<p><em>def </em>get_estimates(<em>self</em>) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; list_of_estimates = []<br /> <br /> &nbsp;&nbsp;&nbsp; <em>for </em>measurement <em>in </em><em>self</em>.__measurements:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>self</em>.__measurement = measurement<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>self</em>.make_basic_calculations()<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; list_of_estimates.append(<em>self</em>.__estimate)<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>list_of_estimates</p>
<p>This method iterates through all measurements in the list of measurements that are passed when having been creating KalmanFilter() object. <em>make_basic_calculations() </em>does exactly what it stands for; its definition is provided below. After every calculation new estimate is appended in the list of estimates that will be returned in the result.</p>
<h4><a name="_Toc47164698"></a>Definition of make_basic_calculations()</h4>
<p><em>def </em>make_basic_calculations(<em>self</em>):<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.__kalman_gain = <em>self</em>.__calculate_kalman_gain()<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.__estimate = <em>self</em>.__calculate_estimate()<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.__error_in_estimate = <em>self</em>.__calculate_error_in_estimate()</p>
<p>This method uses other simple methods to produce Kalman Filter calculations for a one-dimension model and make an estimation. The description of every method is given below.</p>
<h4><a name="_Toc47164699"></a>Definition of __calculate_kalman_gain()</h4>
<p><em>def </em>__calculate_kalman_gain(<em>self</em>) -&gt; <em>float</em>:<br /> &nbsp;&nbsp;&nbsp; <em>return </em><em>self</em>.__error_in_estimate / (<em>self</em>.__error_in_estimate + <em>self</em>.__error_in_measurement)</p>
<p>&nbsp;</p>
<h4><a name="_Toc47164700"></a>Definition of __calculate_estimate()</h4>
<p><em>def </em>__calculate_estimate(<em>self</em>) -&gt; <em>float</em>:<br /> &nbsp;&nbsp;&nbsp; <em>return </em><em>self</em>.__estimate + <em>self</em>.__kalman_gain * (<em>self</em>.__measurement - <em>self</em>.__estimate)</p>
<p>&nbsp;</p>
<h4><a name="_Toc47164701"></a>Definition of __calculate_error_in_estimate()</h4>
<p><em>def </em>__calculate_error_in_estimate(<em>self</em>) -&gt; <em>float</em>:<br /> &nbsp;&nbsp;&nbsp; <em>return </em>(1 - <em>self</em>.__kalman_gain) * <em>self</em>.__error_in_estimate</p>
<p>&nbsp;</p>
<h4><a name="_Toc47164702"></a>Definition of get_lists_of_estimates()</h4>
<p><em>def </em>get_lists_of_estimates(lists_of_measurements: <em>list</em>, error_in_estimate: <em>float</em>,<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; error_in_measurement: <em>float</em>) -&gt; <em>list</em>:<br /> &nbsp;&nbsp;&nbsp; lists_of_estimates = []<br /> <br /> &nbsp;&nbsp;&nbsp; <em>for </em>measurements <em>in </em>lists_of_measurements:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; initial_estimate = KalmanFilter.__get_initial_estimate(measurements)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; kf = KalmanFilter(error_in_estimate, initial_estimate, error_in_measurement, measurements)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; lists_of_estimates.append(kf.get_estimates())<br /> <br /> &nbsp;&nbsp;&nbsp; <em>return </em>lists_of_estimates</p>
<p>This method iterates through lists of measurements, automatically creates initial estimate, KalmanFilter object, and append list of estimates to final list that will be returned in the result.</p>
<h4><a name="_Toc47164703"></a>Definition of __get_initial_estimate()</h4>
<p><em>def </em>__get_initial_estimate(measurements: <em>list</em>) -&gt; <em>float</em>:<br /> &nbsp;&nbsp;&nbsp; <em>return </em>measurements[-1] + (<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; measurements[-1] - measurements[-2])</p>
<p>This method returns an average of last two elements.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h1><a name="_Toc47164704"></a><a name="_Toc33784684"></a>7.&nbsp;&nbsp;&nbsp; Plots</h1>
<p>This program has <strong>GraphEditor.py </strong>that uses <strong>matplotlib </strong>module to create plots.</p>
<p>To create one plot or plots for a list of estimates, it is needed to create an object of <strong><em>class GraphEditor</em></strong> and use correct proper methods:</p>
<p>graph = GraphEditor(estimates, measurements, value, station_code, period)<br /> graph.create_est_and_meas_plot()</p>
<p>&nbsp;</p>
<p>Also, there are variants of plots that can be created:</p>
<p>graph.create_est_plot()<br /> graph.create_meas_plot()</p>
<p>Creating separate plots for estimates and measurements.</p>
<p>To show the created plot, the following method should be used:</p>
<p>graph.show_plot()</p>
<p>It will display a plot in the program that are used, but if need to save the created plot, this method should be used for saving:</p>
<p>graph.save_plot()</p>
<p>&nbsp;</p>
<p>IMPORTANT NOTE!</p>
<p>Don&rsquo;t show plot and then try to save it, it will not work. Separately these methods work just fine.</p>
<h3><a name="_Toc47164705"></a><a name="_Toc33784685"></a>Definitions</h3>
<h4><a name="_Toc47164706"></a>Definition of GraphEditor __init__ also known as class constructor</h4>
<p><em>def </em><em>__init__</em>(<em>self</em>, estimates: <em>list</em>, measurements: <em>list</em>, value: <em>str</em>, station_name: <em>str</em>, period: <em>str</em>, accuracy=<em>None</em>):<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.estimates = estimates<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.measurements = measurements<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.value = value<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.station_name = station_name<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.period = period<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.accuracy = accuracy<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.plt = <em>None</em></p>
<p>Initialization of class object and defining variables.</p>
<h4><a name="_Toc47164707"></a>Definition of create_est_and_meas_plot()</h4>
<p><em>def </em>create_est_and_meas_plot(<em>self</em>):<br /> &nbsp;&nbsp;&nbsp; plt.plot(<em>self</em>.estimates, label='estimates', color='blue')<br /> &nbsp;&nbsp;&nbsp; plt.plot(<em>self</em>.measurements, label='measurements', color='orange')<br /> &nbsp;&nbsp;&nbsp; plt.title(<em>self</em>.station_name + ', Period: ' + <em>self</em>.period)<br /> &nbsp;&nbsp;&nbsp; plt.ylabel(<em>self</em>.value)<br /> &nbsp;&nbsp;&nbsp; plt.xlabel('Observations')<br /> &nbsp;&nbsp;&nbsp; plt.legend()<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.plt = plt</p>
<p>This method setups settings for plot such as title, legend, labels for x-y axis, and saves plot for further usage like saving or showing in the program.</p>
<h4><a name="_Toc47164708"></a>Definition of create_est_plot()</h4>
<p><em>def </em>create_est_plot(<em>self</em>):<br /> &nbsp;&nbsp;&nbsp; plt.plot(<em>self</em>.estimates, color='blue')<br /> &nbsp;&nbsp;&nbsp; plt.title('Estimates: ' + <em>self</em>.station_name + ', Period: ' + <em>self</em>.period)<br /> &nbsp;&nbsp;&nbsp; plt.ylabel(<em>self</em>.value)<br /> &nbsp;&nbsp;&nbsp; plt.xlabel('Observations')<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.plt = plt</p>
<p>This method does the same things but only for estimations.</p>
<h4><a name="_Toc47164709"></a>Definition of create_meas_plot()</h4>
<p><em>def </em>create_meas_plot(<em>self</em>):<br /> &nbsp;&nbsp;&nbsp; plt.plot(<em>self</em>.measurements, color='orange')<br /> &nbsp;&nbsp;&nbsp; plt.title('Measurements: ' + <em>self</em>.station_name + ', Period: ' + <em>self</em>.period)<br /> &nbsp;&nbsp;&nbsp; plt.ylabel(<em>self</em>.value)<br /> &nbsp;&nbsp;&nbsp; plt.xlabel('Observations')<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.plt = plt</p>
<p>This method creates a plot for measurement in the way, like two previous methods.</p>
<h4><a name="_Toc47164710"></a>Definition of show_plot()</h4>
<p><em>def </em>show_plot(<em>self</em>):<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.plt.show()</p>
<p>Simple method that shows plot in program.</p>
<h4><a name="_Toc47164711"></a>Definition of save_plot()</h4>
<p><em>def </em>save_plot(<em>self</em>):<br /> &nbsp;&nbsp;&nbsp; <em>self</em>.plt.savefig('Plot{}.pdf'.format(GraphEditor.index), dpi=300)<br /> &nbsp;&nbsp;&nbsp; GraphEditor.index += 1</p>
<p>A method that saves plot to project folder with settings that were passed as arguments for <em>savefig()</em> method.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h1><a name="_Toc47164712"></a>8.&nbsp;&nbsp;&nbsp; ARIMA</h1>
<p>&nbsp;</p>
<h2><a name="_Toc47164713"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; I.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ARIMA main</h2>
<p>&nbsp;</p>
<p>For making forecast with ARIMA model is used <strong>Arima_Main.py </strong>with modules such as <strong>pandas</strong> for working with data frames and data series, <strong>numpy </strong>and <strong>ARIMA </strong>from <strong>statsmodels.tsa.arima_model</strong>. For making forecast and receive all information that was used for forecasting, it is needed to create class <strong><em>Arima_Main</em></strong> and use correct method as shown here:</p>
<p>data_points_for_forecast, arima_model_order, steps, forecast = Arima_Main(series_of_measurements, steps, optimize).get_arima_forecast()</p>
<p>&nbsp;</p>
<p>IMPORTANT NOTE!</p>
<p>&nbsp;</p>
<p><em>series_of_measurements</em> must contain only one data column and one index column, because for making forecast are used <em>series_of_measurements</em> values, it means it can be used only DataFrame with one data column of just Series.</p>
<p>&nbsp;</p>
<p><em>Definition of </em><em>get_arima_forecast()</em></p>
<p>def get_arima_forecast(self):<br /> <br /> &nbsp;&nbsp;&nbsp; arima_models_order_and_data_points_dict = Arima_Main.get_all_possible_arima_models_with_data_points(self)<br /> <br /> &nbsp;&nbsp;&nbsp; # dataframe of data points, steps and RMSE<br /> &nbsp;&nbsp;&nbsp; rmse_df = pd.DataFrame()<br /> <br /> &nbsp;&nbsp;&nbsp; rmse_dict = dict()<br /> &nbsp;&nbsp;&nbsp; last_point = len(self.data_series) - 1 - self.steps<br /> <br /> &nbsp;&nbsp;&nbsp; for data_points, order in arima_models_order_and_data_points_dict.items():<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; first_point = last_point - data_points<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_series_copy = self.data_series[first_point:last_point].copy()<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # ----- Make copy of real data for comparing with forecast ----- #<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; station_data_copy_with_steps = self.data_series[last_point - 1:last_point - 1 + self.steps].copy()<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; forecast_list = Arima_Main.make_forecast(order, data_series_copy, self.steps)<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; rmse = Arima_Main.get_forecast_accuracy_with_real_data(forecast_list, station_data_copy_with_steps.values)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; rmse_dict[data_points] = rmse<br /> <br /> &nbsp;&nbsp;&nbsp; rmse_series = pd.Series(rmse_dict)<br /> &nbsp;&nbsp;&nbsp; rmse_df[str(self.steps)] = rmse_series<br /> <br /> &nbsp;&nbsp;&nbsp; rmse_df.reset_index(inplace=True)<br /> &nbsp;&nbsp;&nbsp; rmse_df['order'] = arima_models_order_and_data_points_dict.values()<br /> &nbsp;&nbsp;&nbsp; rmse_df.rename(columns={'index': 'points'}, inplace=True)<br /> &nbsp;&nbsp;&nbsp; rmse_df.set_index(['points', 'order'], inplace=True)<br /> <br /> &nbsp;&nbsp;&nbsp; results = Arima_Main.get_steps_and_points_of_min_rmse(rmse_df)<br /> <br /> &nbsp;&nbsp;&nbsp; data_points_for_forecast = results[0][0]<br /> <br /> &nbsp;&nbsp;&nbsp; steps = int(results[1])<br /> <br /> &nbsp;&nbsp;&nbsp; data_series_copy = self.data_series[- data_points_for_forecast:].copy()<br /> <br /> &nbsp;&nbsp;&nbsp; arima_model_order = Arima_Order(data_series_copy).get_arima_best_order()<br /> <br /> &nbsp;&nbsp;&nbsp; forecast = Arima_Main.make_forecast(arima_model_order, data_series_copy, steps)<br /> <br /> &nbsp;&nbsp;&nbsp; return [data_points_for_forecast, arima_model_order, steps, forecast]</p>
<p>As a result, we get a list, that contains:</p>
<ul>
<li>How much data points must be taken for making forecast.</li>
<li>ARIMA best model&rsquo;s order (p, d, q).</li>
<li>How much steps in the future must be taken for making forecast.</li>
<li>List of forecast values.</li>
</ul>
<p><em>Definition of get_all_possible_arima_models_with_data_points()</em></p>
<p>def get_all_possible_arima_models_with_data_points(self):<br /> &nbsp;&nbsp;&nbsp; if self.optimize:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if len(self.data_series) &lt;= 1000 + self.steps:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; optimize_point = len(self.data_series)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; optimize_point = 400<br /> &nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; optimize_point = len(self.data_series)<br /> &nbsp;&nbsp;&nbsp; arima_models_order_and_data_points_dict = dict()<br /> &nbsp;&nbsp;&nbsp; last_point = len(self.data_series) - 1 - self.steps<br /> &nbsp;&nbsp;&nbsp; process = 0<br /> &nbsp;&nbsp;&nbsp; data_point_range = range(100, optimize_point, 10)<br /> &nbsp;&nbsp;&nbsp; data_point_range_len = len(range(100, optimize_point, 10))<br /> &nbsp;&nbsp;&nbsp; for data_points in data_point_range:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; process += 1<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; first_point = last_point - data_points<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if first_point &lt; 0:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; break<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_series_copy = self.data_series[first_point:last_point].copy()<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; order = Arima_Order(data_series_copy).get_arima_best_order()<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if order == 0:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # print('ARIMA model was NOT DEFINED for', len(data_series_copy), 'observation points')<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print('{:.0f}%'.format(process / data_point_range_len * 100))<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; continue<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # print('ARIMA model with order', order, 'for', len(data_series_copy), 'observation points')<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print('{:.0f}%'.format(process / data_point_range_len * 100))<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; arima_models_order_and_data_points_dict[data_points] = order<br /> <br /> &nbsp;&nbsp;&nbsp; return arima_models_order_and_data_points_dict</p>
<p>This method returns a dictionary with data points and with the best ARIMA model order for this data set. It looks like this:</p>
<p>{ data_points1 : model_order1, data_points2 : model_order2, &hellip; }</p>
<p>or</p>
<p>{ 100 : [1, 2, 1], 110 : [2, 1, 4] &hellip; }</p>
<p><em>&nbsp;</em></p>
<p><em>Definition of get_forecast_accuracy_with_real_data()</em></p>
<p>def get_forecast_accuracy_with_real_data(forecast, actual):<br /> &nbsp;&nbsp;&nbsp; rmse = np.mean((forecast - actual) ** 2) ** .5<br /> &nbsp;&nbsp;&nbsp; return rmse</p>
<p>Returns RMSE as a float value, that characterizes the forecast accuracy with actual data</p>
<p>&nbsp;</p>
<p><em>Definition of</em> <em>make_forecast()</em></p>
<p>def make_forecast(arima_model_order, data_series, steps):<br /> &nbsp;&nbsp;&nbsp; arima_model_station_data = ARIMA(data_series, order=arima_model_order).fit(disp=0)<br /> &nbsp;&nbsp;&nbsp; forecast_list = arima_model_station_data.forecast(steps=steps)[0].tolist()<br /> <br /> &nbsp;&nbsp;&nbsp; return forecast_list</p>
<p>Method uses the best ARIMA model order, that was find before, and returns list of forecast value. The number of received values in the list is equal with steps value.</p>
<p>&nbsp;</p>
<h2><a name="_Toc47164714"></a>&nbsp;&nbsp;&nbsp; II.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ARIMA order</h2>
<p>&nbsp;</p>
<p>To determine ARIMA order is used <strong>ArimaOrder.py</strong> with modules ARIMA from <strong>statsmodels.tsa.arima_model</strong>, <strong>adfuller</strong> from <strong>statsmodels.tsa.stattools </strong>for finding p-value, that indicates if model is stationary or not, <strong>plot_pacf</strong>, <strong>plot_acf</strong> from <strong>statsmodels.graphics.tsaplots</strong> and <strong>pyplot</strong> for showing autocorrelation and partial autocorrelation graphs.</p>
<p><em>Definition of get_d_value_and_ADF_test()</em></p>
<p>def get_d_value_and_ADF_test(self):<br /> </p>
<p>&nbsp;&nbsp;&nbsp; d = 0</p>
<p><br /> &nbsp;&nbsp;&nbsp; try:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; adf_test_results = adfuller(self.data_series.values)<br /> &nbsp;&nbsp;&nbsp; except:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return d<br /> <br /> &nbsp;&nbsp;&nbsp; data_series_diff = self.data_series<br /> &nbsp;&nbsp;&nbsp; while adf_test_results[1] &gt; 0.05 or d == 0:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if d &gt; 2:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d += 1<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # ----- make data stationary and drop NA values ----- #<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_series_diff = data_series_diff.diff().dropna()<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; try:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data_series_diff_values = data_series_diff.values<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; adf_result = adfuller(data_series_diff_values)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; except:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; d -= 1<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return d<br /> <br /> &nbsp;&nbsp;&nbsp; # print('ADF p-value:', adf_result[1])<br /> &nbsp;&nbsp;&nbsp; # print('d:', d)<br /> <br /> &nbsp;&nbsp;&nbsp; # ----- autocorrelation ----- #<br /> &nbsp;&nbsp;&nbsp; #plot_acf(data_diff)<br /> &nbsp;&nbsp;&nbsp; #plt.gcf().autofmt_xdate()<br /> &nbsp;&nbsp;&nbsp; #plt.show()<br /> &nbsp;&nbsp;&nbsp; # ----- partial autocorrelation ----- #<br /> &nbsp;&nbsp;&nbsp; #plot_pacf(data_diff)<br /> &nbsp;&nbsp;&nbsp; #plt.gcf().autofmt_xdate()<br /> &nbsp;&nbsp;&nbsp; #plt.show()<br /> <br /> &nbsp;&nbsp;&nbsp; return d</p>
<p>This method is used to define d value for ARIMA model (p, d , q) order. d represents the number of times that the data have to be &ldquo;differenced&rdquo; to produce a stationary signal (i.e., a signal that has a constant mean over time). This captures the &ldquo;integrated&rdquo; nature of ARIMA. If d=0, this means that our data does not tend to go up/down in the long term (i.e., the model is already &ldquo;stationary&rdquo;). In this case, then technically you are performing just ARMA, not AR-I-MA. If p is 1, then it means that the data is going up/down linearly. If p is 2, then it means that the data is going up/down exponentially. To define d value is used&nbsp; Augmented Dickey-Fuller test with p-value:</p>
<ul>
<li>p-value &gt; 0.05: the data has a unit root and is non-stationary.</li>
<li>p-value &lt;= 0.05: the data does not have a unit root and is stationary.</li>
<li>The more negative is ADF Statistic, the more likely we have a stationary dataset.</li>
</ul>
<p>&nbsp;</p>
<p><em>Definition of</em> <em>get_arima_best_order()</em></p>
<p>def get_arima_best_order(self):<br /> <br /> &nbsp;&nbsp;&nbsp; d = Arima_Order.get_d_value_and_ADF_test(self)<br /> <br /> &nbsp;&nbsp;&nbsp; p_values = range(0, 5)<br /> &nbsp;&nbsp;&nbsp; q_values = range(0, 5)<br /> <br /> &nbsp;&nbsp;&nbsp; aic_dict = dict()<br /> <br /> &nbsp;&nbsp;&nbsp; for p in p_values:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for d in range(d, 2):<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for q in q_values:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; order = (p, d, q)<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; try:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; arima_station_model = ARIMA(self.data_series, order).fit(disp=0)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; aic = arima_station_model.aic<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # print('ARIMA%s aic = %.5f' % (order, aic))<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if [p, d, q] == [0, 0, 0] or [p, d, q] == [0, 1, 0] or [p, d, q] <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; == [0, 1, 1]:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if aic not in aic_dict:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; aic_dict[aic] = order<br /> <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; except:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # print('ARIMA%s aic not defined' % (order,))<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; continue<br /> <br /> &nbsp;&nbsp;&nbsp; # if aic_dict is empty<br /> &nbsp;&nbsp;&nbsp; # it is impossible to create arima model for this data set<br /> &nbsp;&nbsp;&nbsp; if len(aic_dict) == 0:<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0<br /> <br /> &nbsp;&nbsp;&nbsp; min_val = min(aic_dict.keys())<br /> &nbsp;&nbsp;&nbsp; # print('min AIC value', min_val)<br /> &nbsp;&nbsp;&nbsp; # print('ARIMA model was created with order', aic_dict[min_val])<br /> <br /> &nbsp;&nbsp;&nbsp; # ----- ARIMA (p, d, q) ----- #<br /> &nbsp;&nbsp;&nbsp; p = aic_dict[min_val][0]<br /> &nbsp;&nbsp;&nbsp; q = aic_dict[min_val][2]<br /> <br /> &nbsp;&nbsp;&nbsp; return [p, d, q]</p>
<p>This method returns best ARIMA model order using Akaike information criterion for characterizing and d value from <em>d_value_and_ADF_test </em>method. AIC estimates the relative amount of information lost by a given model: the less information a model loses, the higher the quality of that model.</p>
<h1><a name="_Toc47164715"></a><a name="_Toc33784686"></a>9. API</h1>
<p>The fundamental representation of API that can be used as Web Service of this framework.</p>
<p>Five routes are used:</p>
<ol>
<li>/get/estimates/all</li>
</ol>
<p>&nbsp;</p>
<ol start="2">
<li>/get/estimates</li>
</ol>
<p>&nbsp;</p>
<ol start="3">
<li>/get/accuracies</li>
</ol>
<p>&nbsp;</p>
<ol start="4">
<li>/get/forecast/arima</li>
</ol>
<p>&nbsp;</p>
<ol start="5">
<li>/get/forecast/arima/time_period</li>
</ol>
<p>All these requests have essential arguments and secondary ones. Every request has an essential argument <em>value</em>.</p>
<h2><a name="_Toc47164716"></a><a name="_Toc33784687"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; I.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /get/estimates/all</h2>
<p>The first route returns JSON with estimates for all stations and chosen value.</p>
<p>Essential argument: <em>value</em></p>
<p>Secondary argument: <em>measurements</em></p>
<p><a name="_Toc33784688"></a>For example:</p>
<p><a href="http://127.0.0.1:5001/get/estimates/all?value=Dew%20Point">/get/estimates/all?value=Dew%20Point</a></p>
<p>The server will return JSON with estimates for all datasets of Dew Point that are suitable for estimation.</p>
<p><a href="http://127.0.0.1:5001/get/estimates/all?value=Dew%20Point&amp;measurements=true">/get/estimates/all?value=Dew%20Point&amp;measurements=true</a></p>
<p>If add <em>measurements </em>argument and set it to true, then JSON will contain measurements for every station as well.</p>
<h2><a name="_Toc47164717"></a><a name="_Toc33784689"></a>&nbsp;&nbsp;&nbsp; II.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /get/estimates</h2>
<p>The second route can return JSON with estimates for the exact station or stations.</p>
<p>Essential argument: <em>value </em>and<em> stations</em></p>
<p>Secondary argument: <em>measurements</em></p>
<p><a name="_Toc33784690"></a>For example:</p>
<p><a href="http://127.0.0.1:5001/get/estimates?value=Dew%20Point&amp;stations=LV01">/get/estimates?value=Dew%20Point&amp;stations=LV01</a></p>
<p>This request will return JSON with estimates of Dew Point for station LV01. To get estimates for many stations adding their code to <em>stations </em>argument separated by <em>comma, </em>like below:</p>
<p><a href="http://127.0.0.1:5001/get/estimates?value=Dew%20Point&amp;stations=LV01,LV02,LV03">/get/estimates?value=Dew%20Point&amp;stations=LV01,LV02,LV03</a></p>
<p>If needed to get measurements too, just add <em>measurements </em>argument and set it to true to URL:</p>
<p><a href="http://127.0.0.1:5001/get/estimates?value=Dew%20Point&amp;stations=LV01,LV02,LV03&amp;measurements=true">/get/estimates?value=Dew%20Point&amp;stations=LV01,LV02,LV03&amp;measurements=true</a></p>
<h2><a name="_Toc47164718"></a><a name="_Toc33784691"></a>&nbsp;III.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /get/accuracies</h2>
<p>Third route is for getting accuracy of estimation.</p>
<p>Essential argument: <em>value, stations</em></p>
<p>Secondary argument: None</p>
<p><a name="_Toc33784692"></a>For example:</p>
<p><a href="http://127.0.0.1:5001/get/accuracies?value=Dew%20Point&amp;stations=LV01">/get/accuracies?value=Dew%20Point&amp;stations=LV01</a></p>
<p><a href="http://127.0.0.1:5001/get/accuracies?value=Dew%20Point&amp;stations=LV01,LV02,LV03">/get/accuracies?value=Dew%20Point&amp;stations=LV01,LV02,LV03</a></p>
<p>These requests will return JSON with accuracies for stations and value that are set up in request arguments.</p>
<h2>&nbsp; IV.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;<a name="_Toc47164719"></a>/get/forecast/arima</h2>
<p>Is used for getting forecast values using station data.</p>
<p>Essential argument: value, station, steps and optimize.</p>
<p>For <em>value</em> argumest can be used &ldquo;Dew Point&rdquo;, &ldquo;Air Temperature&rdquo; and etc.</p>
<p><em>Steps</em> value means how many points ahead will be made forecast.</p>
<p><em>Optimize</em> option is used to determine the best model using only last 1000 data point. In otherwise the program uses full data and it may take much more time and not make sense.</p>
<p>For example:</p>
<p><a href="http://127.0.0.1:5001/get/forecast/arima?value=Dew%20Point&amp;station=LV01&amp;steps=5&amp;optimize=true">/get/forecast/arima?value=Dew%20Point&amp;station=LV01&amp;steps=5&amp;optimize=true</a></p>
<h2><a name="_Toc47164720"></a>&nbsp;&nbsp;&nbsp; V.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /get/forecast/arima/time_period</h2>
<p>Is used for getting forecast values using station data and using time period with date from and date till.</p>
<p>Essential argument: value, station, steps, optimize, date_from and date_till.</p>
<p>Date value can be inputed in two formats:</p>
<p>YYYY-MM-DD and time value will be automatically set to 00:00</p>
<p>YYYY-MM-DD_HH:MM</p>
<p>For example:</p>
<p><a href="http://127.0.0.1:5001/get/forecast/arima/time_period?value=Dew%20Point&amp;station=LV01&amp;steps=5&amp;optimize=true&amp;date_from=2020-02-10_12:00&amp;date_till=2020-04-15_14:00">/get/forecast/arima/time_period?value=Dew%20Point&amp;station=LV01&amp;steps=5&amp;optimize=true&amp;date_from=2020-02-10_12:00&amp;date_till=2020-04-15_14:00</a></p>
<p><a href="http://127.0.0.1:5001/get/forecast/arima/time_period?value=Dew%20Point&amp;station=LV01&amp;steps=5&amp;optimize=true&amp;date_from=2020-02-10&amp;date_till=2020-04-15">/get/forecast/arima/time_period?value=Dew%20Point&amp;station=LV01&amp;steps=5&amp;optimize=true&amp;date_from=2020-02-10&amp;date_till=2020-04-15</a></p>
