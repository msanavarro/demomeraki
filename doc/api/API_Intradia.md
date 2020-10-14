**API INTRA DIA  Meraki ISAT DEMO**
----


Este API regresa la cantidad de personas en sitio a una fecha y hora determinada

* **/v1/report/intradia**


* **Method:**

  `GET`


*  **URL Params**

   **Required:**

   `date_hour=[date]'YYYY-mm-dd HH'`<br />

*   **Optional:**

   `NA`

* **Data Params**

   `NA`

* **Success Response:**

  * **Code:** 200 <br />
    **type:** 23 <br />
    **Content:** `{
        date_hour:[fecha],
        floor0:[int],
        floor1:[int],
        floor2:[int],
        floor3:[int]
        }
      }`

* **Error Response:**

  * **Code:** 400 Bad Request <br />
    * **Content:** `{ errorid: 1 , error : "Error de parametros" }` <br/>
    * **Content:**  `{ errorid: 2, error : "formato de fecha erroneo" }`<br/>
    * **Content:** `{ errorid: 3, error : "fecha inicial mayor que fecha final" }` <br/>
    * **Content:** `{ errorid: 4, error : "piso fuera de rango" }` <br/>

  OR

  * **Code:** 403 Forbidden <br />
    **Content:** `{ error : "credenciales erroneas" }`

  OR

  * **Code:** 404 Not Found <br />
    **Content:** `{ error : "el recurso que esta buscando no esta disponible" }`

  OR

  * **Code:** 500 server error <br />
    **Content:** `{ error : "error en servidor" }`

  OR

  * **Code:** 501 not implemented <br />
    **Content:** `{ error : "el servidor no tiene un metodo para atender esta solicitud" }`

* **Sample Call:**

  `curl http://server:port//v1/report/intradia?`
  `piso=mac=addr&`
  `fecha_ini=fechainicial&`
  `fecha_fin=fechafinal`


* **Notes:**
