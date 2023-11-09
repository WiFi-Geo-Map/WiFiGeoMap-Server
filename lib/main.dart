import 'dart:async';
import 'dart:developer' as developer;
import 'dart:io';

import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:network_info_plus/network_info_plus.dart';
import 'package:permission_handler/permission_handler.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        useMaterial3: true,
        colorSchemeSeed: const Color(0x9f4376f8),
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, this.title});

  final String? title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String _connectionStatus = 'Unknown';
  final NetworkInfo _networkInfo = NetworkInfo();

  @override
  void initState() {
    super.initState();
    _initNetworkInfo();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('BSSID & SSID'),
        elevation: 4,
      ),
      body: Center(
          child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          const Text(
            'Network info',
            style: TextStyle(
              fontSize: 16,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 16),
          Text(_connectionStatus),
          Center(
        child: ElevatedButton(
          onPressed: _initNetworkInfo,
          child: const Text("Refresh"),
        ),)
        ],
      )),
    );
  }

  Future<void> _initNetworkInfo() async {
    String? wifiName, wifiBSSID;

    // Request location permissions
    final locationStatus = await Permission.location.request();
    if (locationStatus.isGranted) {
      try {
        if (!kIsWeb && (Platform.isIOS || Platform.isAndroid)) {
          wifiName = await _networkInfo.getWifiName();
          wifiBSSID = await _networkInfo.getWifiBSSID();
        } else {
          wifiName = await _networkInfo.getWifiName();
          wifiBSSID = await _networkInfo.getWifiBSSID();
        }
      } on PlatformException catch (e) {
        developer.log('Failed to get network information', error: e);
        wifiName = 'Failed to get network information';
        wifiBSSID = 'Failed to get network information';
      }
    } else {
      wifiName = 'Location permission not granted';
      wifiBSSID = 'Location permission not granted';
    }

    setState(() {
      _connectionStatus = 'Wifi Name: $wifiName\n'
          'Wifi BSSID: $wifiBSSID\n';
    });
  }
}
