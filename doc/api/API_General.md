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
    **Content:** `[
          {
          "macaddr":[str], 
          "name":[str],
          "timesseen":[int],
          "maxstay":[float],
          "maxdate":[date],
          "minsstay":[float],
          "mindate":[date],
          "averagestay":[float]
          }
    ]`



* **Error Response:**

  * **Code:** 400 Bad Request <br />
    * **Content:** `{ errorid: 1 , error : "Error de parametros" }` <br/>
    * **Content:**  `{ errorid: 2, error : "formato de fecha erroneo" }`<br/>
    * **Content:** `{ errorid: 3, error : "fecha inicial mayor que fecha final" }` <br/>
 <br/>
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
