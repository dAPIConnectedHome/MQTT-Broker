# MQTT-Broker

bathroom/kitchen/livingroom/terrace/garden
    skripte, die das Senden von einzelnen Sensoren simulieren. Dabei wurde hier jeweils eine feste objectID eingetragen und die Sensordaten werden random erstellt.
    Somit können auch einzelne Räume gestartet werden.
    
complete 
    Skript, dass alle Räume (oben genannt) gleichzeitig in parallel laufenden Threads startet
    
Dummythread
    Client, der immer läuft. Dieser ist für die Vergabe von objectIDs zuständig. Meldet sich ein neuer Client unter einem bestimmten Topic, so wird diesem eine neue objectID 
    zugewiesen. Es wird geprüft, ob die neue objectID bereits vorhanden ist, wenn nicht, wird diese in eine Liste eingetragen.
    Beinhaltet die feste defaultID des neuen Clients ein A oder S, so wird auch ein A oder S der objectID zugewiesen, um einen Sensor von einem Aktor unterscheiden zu können.
    Die Kommunikation läuft dann ausschließlich über das Topic shlogo/"objectID"/set/.
    Da der Dummythread in einer Dauerschleife läuft, ist es immer wieder möglich, neue Clients zuzuweisen.
    
    
new_Client
    Hier wird das Anbinden eines neuen Client getestet. Mit einer festen defaultID meldet er sich auf ein bestimmtes Topic. Eine objectID wird vom Dummythread zurückgesendet.
    Zudem werden wichtige Informationen des Clients gesendet, um sie in der Datenbank zuordnen zu können.
    In diesem Fall ist der neue Client ein Aktor, welcher eine LED ein und aus schaltet.
    
    
