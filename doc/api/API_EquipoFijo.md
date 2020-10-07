**API Alarma Equipo Fijo DEMO ISAT Meraki**
----
Alarma que se activa cuando un equipo que se supone fijo deja de aparecer en los datos recibidos desde los APs de Meraki.
Para recibir la alarma primero es necesario registrarse en la base de datos del Webhook mediante la llamada POST a **/v1/report/webhookregistry**, documentada por separado.

* **https://cliente:puerto/ejemplo/abc**


* **Method:**

  `POST`


*  **URL Params**

   **Required:**

   **Content:** `{
       mac_adrr: 'a1:b2:c3:d4:e5:f6',
       nombre: 'mi aparato favorito',
       fechahora_desconexion: '2020-09-17 00:00:00'
        }`

   **Optional:**

   `NA`

* **Data Params**

   `NA`

* **Success Response:**

  * **Code:** 200 <br />

* **Error Response:**

  * **Code:** 400 Bad Request <br />
    * **Content:** `{ errorid: 1 , error : "Error de parametros" }` <br/>
    * **Content:**  `{ errorid: 2, error : "formato de fecha erroneo" }`<br/>
 <br/>

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


* **Sample Call[POST]:**<br/>
curl -L -X POST 'https://cliente:puerto/ejemplo/abc' -H 'Content-Type: application/json' --data-raw '{
       mac_adrr: '\''a1:b2:c3:d4:e5:f6'\'',
       nombre: '\''mi aparato favorito'\'',
       fechahora_desconexion: '\''2020-09-17 00:00:00'\''
}'

* **Sample Call[GET]:**`
curl -L -X GET 'https://cliente:puerto/ejemplo/abc?mac_adrr=a1:b2:c3:d4:e5:f6&nombre=mi%20aparato%20favorito&fechahora_desconexion=2020-09-17%2000:00:00'
`

* **Notes:**
