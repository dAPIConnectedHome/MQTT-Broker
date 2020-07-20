# MQTT-Broker

bathroom/kitchen/livingroom/terrace/garden
    skripte, die das Senden von einzelnen Sensoren simulieren. Dabei wurde hier jeweils eine feste objectID eingetragen und die Sensordaten werden random erstellt
    
complete 
    Skript, dass alle Räume (oben genannt) gleichzeitig in parallel laufenden Threads startet
    
Dummythread
    Client, der immer läuft. Dieser ist für die Vergabe von objectIDs zuständig. Meldet sich ein neuer Client unter einem bestimmten Topic, so wird diesem eine neue objectID 
    zugewiesen. Es wird geprüft, ob die neue objectID bereits vorhanden ist, wenn nicht, wird diese in eine Liste eingetragen.
    Die Kommunikation läuft dann ausschließlich über das Topic shlogo/"objectID".
    
