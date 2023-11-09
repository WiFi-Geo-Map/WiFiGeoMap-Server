void main() {
  String data = """
6	LH4-AP	38:17:c3:f2:4b:70	
38:17:c3:f2:4b:71	
38:17:c3:f2:4b:72	
38:17:c3:f2:4b:73	
38:17:c3:f2:4b:60	
38:17:c3:f2:4b:61	
38:17:c3:f2:4b:62	
38:17:c3:f2:4b:63	
""";

  List<String> lines = data.trim().split('\n');
  String ssid = "";
  List<String> bssids = [];

  for (String line in lines) {
    List<String> parts = line.split('\t');
    if (parts.length >= 3) {
      String currentSSID = parts[1];
      String bssid = parts[2];

      if (currentSSID != ssid) {
        if (ssid == "LH4-AP") {
          // Map the SSID to its BSSIDs
          print('SSID: $ssid, BSSIDs: $bssids');
        }
        ssid = currentSSID;
        bssids = [];
      }
      bssids.add(bssid);
    }
  }

  if (ssid == "LH4-AP") {
    // Map the last SSID to its BSSIDs
    print('SSID: $ssid, BSSIDs: $bssids');
  }
}
