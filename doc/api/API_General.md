**API Reporte General DEMO ISAT Meraki**
----
Reporte de resultados general de afluencia de personal

* **/v1/report/general**


* **Method:**

  `GET`


*  **URL Params**

   **Required:**

   `mac=[alphanumeric]`

   `fecha_ini=[date]`

   `fecha_fin=[date]`

   **Optional:**

   `NA`

* **Data Params**

   `NA`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
        mac_adrr: 12:32:43:23:32:EE
        nombre: "Alejandro Jose Sanchez"
        num_entradas : 12,
        num_salidas: 5,
        timempo_promedio: 3hr
        tiempo_max = 5hr
        tiempo_min = .5hr
        dia_t_max = 12/08/2020
        dia_t_min = 13/08/2020
         }`



* **Error Response:**

  * **Code:** 400 Bad Request <br />
    * **Content:** `{ errorid: 1 , error : "Error de parametros" }` <br/>
    * **Content:**  `{ errorid: 2, error : "formato de fecha erroneo" }`<br/>
    * **Content:** `{ errorid: 3, error : "fecha inicial mayor que fecha final" }` <br/>
 <br/>

  OR

  * **Code:** 404 Not Found <br />
    **Content:** `{ error : "error en metodo" }`

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

  `curl http://server:port/v1/report/general?`<br />
    `mac=mac=addr&`<br />
    `fecha_ini=fechainicial&`<br />
    `fecha_fin=fechafinal`

* **Notes:**
