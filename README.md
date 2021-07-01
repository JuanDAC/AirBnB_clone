# AirBnB clone
![UML](documents/uml.png)
## Description

The implementation of the CRUD (create, read, update and delete) interface in a terminal on Python 3.4 <sub>[more](https://en.wikipedia.org/wiki/crud)</sub>

## Folder hierarchy

```Python
AirBnB
├── models
│   ├── engine
│   │   └── file_storage.py
│   │
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
│
├── tests
│   ├── test_models
│   │   ├── test_engine 
│   │   │   └── test_file_storage.py
│   │   │
│   │   └── test_base_model.py
│   │
│   └── test_console.py
│
└── console.py
```

|Command| Description |
|:--|:--:|
| **quit or EOF** | Exits the program |
| **Usage** | By itself |

|Command| Description |
|:--|:--:|
| **help** | Provides a text describing how to use a command.  |
| **Usage** | By itself --or-- **help <command\>** |

|Command| Description |
|:--|:--:|
| **create** | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`.  Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. |
| **Usage** | **create <class name\>**|

|Command| Description |
|:--|:--:|
| **show** | Prints the string representation of an instance based on the class name and `id`  |
| **Usage** | **show <class name\> <id\>** <br> --or-- <br> **<class name\>.show(<id\>)**|

|Command| Description |
|:--|:--:|
| **destroy** | Deletes an instance based on the class name and `id` (saves the change into a JSON file).  |
| **Usage** | **destroy <class name\> <id\>** <br> --or-- <br> **<class name>.destroy(<id>)** |

|Command| Description |
|:--|:--:|
| **all** | Prints all string representation of all instances based or not on the class name.  |
| **Usage** | By itself or **all <class name\>** <br> --or-- <br> **<class name\>.all()** |

|Command| Description |
|:--|:--:|
| **update** | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file).  |
| **Usage** | **update <class name\> <id\> <attribute name\> "<attribute value\>"** <br> ---or--- <br> **<class name\>.update(<id\>, <attribute name\>, <attribute value\>)** <br> --or-- <br> **<class name\>.update(<id\>, <dictionary representation\>)**|

|Command| Description |
|:--|:--:|
| **count** | Retrieve the number of instances of a class.  |
| **Usage** | **<class name\>.count()** |

## Base and objectsd properties 

|             	| Public Instance Attributes 	| Public Instance Methods                 	| Public Class Attributes                                                                                                	| Private Class Attributes 	|
|-------------	|----------------------------	|-----------------------------------------	|------------------------------------------------------------------------------------------------------------------------	|--------------------------	|
| BaseModel   	|```id created_at updated_at ```  	|``` save to_dict```                            	|                                                                                                                        	|                          	|
| FileStorage 	|                            	|```all new save reload (n)delete (n)update ```	|                                                                                                                        	|```__file_path __objects ```   	|
| User        	|```Inherits from BaseModel ```   	|                                         	|```email password first_name last_name ```                                                                                   	|                          	|
| State       	|```Inherits from BaseModel ```   	|                                         	|```name                                                                                                                 ```  	|                          	|
| City        	|```Inherits from BaseModel```    	|                                         	|```state_id name```                                                                                                          	|                          	|
| Amenity     	|```Inherits from BaseModel```    	|                                         	|```name ```                                                                                                                  	|                          	|
| Place       	|```Inherits from BaseModel```    	|                                         	|```city_id user_id name description number_rooms number_bathrooms max_guest price_by_night latitude longitude amenity_ids``` 	|                          	|
| Review      	|```Inherits from BaseModel```    	|                                         	|```place_id user_id text ```                                                                                                 	|     ""                       	|




## Interactive and Non-interactive

In **Interactive mode**, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.
* *interactive* mode  🤩:

---

```
$ ./console.py
(hbnb) help

EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

---

* *non-interactive* mode 😜:  

---
```
$ echo "help" | ./console.py
(hbnb)

EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

EOF  help  quit
(hbnb) 
$
```

## Authors ✒️
<details  style="user-select: none;">
	<summary>
		<strong style="user-select: none;cursor: pointer;">Edher Ramirez</strong> - <a href="https://github.com/Edheramirez" target="_blank">Edheramirez</a>
	</summary>
	<img align="center" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Edheramirez&layout=compact&theme=vue&langs_count=6" alt="adri-er github stats"/>
</details>

<details  style="user-select: none;">
	<summary>
		<strong style="user-select: none;cursor: pointer;">Juan David Avila</strong> - <a href="https://github.com/JuanDAC" target="_blank">JuanDAC</a>
	</summary>
	<img align="center" src="https://github-readme-stats.vercel.app/api/top-langs/?username=JuanDAC&layout=compact&theme=vue&langs_count=6" alt="adri-er github stats"/>
</details>


