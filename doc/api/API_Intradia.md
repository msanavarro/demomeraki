**API INTRA DIA  Meraki ISAT DEMO**
----


Este API regresa la cantidad de personas en sitio por hora de multiples fechas y filtrado por piso

* **/v1/report/intradia**


* **Method:**

  `GET`


*  **URL Params**

   **Required:**

   `piso=[numeric]`<br />
   `fecha_ini=[date]`<br />
   `fecha_fin=[date]`<br />

piso = [0,1,2,3] : donde 0 = todos los pisos, 1 = piso 1, 2= piso 2, etc.

*   **Optional:**

   `NA`

* **Data Params**

   `NA`

* **Success Response:**

  * **Code:** 200 <br />
    **type:** 23 <br />
    **Content:** `{
        piso:0
        fecha: 12/12/2020
        pico_de_personas : 20,
        hora_pico_personas: 11,
        registro_inicial: 8:00,
        registro_intradia: {
          hora0: 0,
          hora1: 0,
          hora2: 0,
          hora3: 0,
          hora4: 0,
          hora5: 0,
          hora6: 0,
          hora7: 1,
          hora8: 5,
          hora9: 10,
          hora10: 6,
          hora11: 20,
          hora12: 20,
          hora13: 16,
          hora14: 17,
          hora15: 15,
          hora16: 11,
          hora17: 10,
          hora18: 5,
          hora19: 4,
          hora20: 1,
          hora21: 1,
          hora22: 0,
          hora23: 0
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
