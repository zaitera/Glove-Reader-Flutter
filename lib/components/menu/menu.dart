import 'package:flutter/material.dart';
import 'package:flutter_blue/flutter_blue.dart';

import 'package:glove_reader/screens/BluetoothOffScreen/BluetoothOffScreen.dart';
import 'package:glove_reader/screens/FindDevicesScreen/FindDevicesScreen.dart';

/// This is the stateful widget that the main application instantiates.
class Menu extends StatefulWidget {
  Menu({Key key}) : super(key: key);

  @override
  _MenuState createState() => _MenuState();
}

/// This is the private State class that goes with Menu.
class _MenuState extends State<Menu> {
  int _selectedIndex = 0;
  static const TextStyle optionStyle =
      TextStyle(fontSize: 30, fontWeight: FontWeight.bold);

  static List<Widget> _widgetOptions = <Widget>[
    Text(
      'Index 1: Home',
      style: optionStyle,
    ),
    StreamBuilder<BluetoothState>(
        stream: FlutterBlue.instance.state.asBroadcastStream(
          onListen: (subscription) {
            return;
          },
          onCancel: (subscription) {
            return;
          },
        ),
        initialData: BluetoothState.unknown,
        builder: (c, snapshot) {
          final state = snapshot.data;
          if (state == BluetoothState.on) {
            return FindDevicesScreen();
          }
          return BluetoothOffScreen(state: state);
        }),
    Text(
      'Index 2: Chart',
      style: optionStyle,
    ),
  ];

  // void _blueToothState(isItOn) {
  //   setState(() {
  //     _isBluetoothOn = isItOn;
  //   });
  // }

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: _widgetOptions.elementAt(_selectedIndex),
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Home',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.bluetooth),
            label: 'BLE',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.multiline_chart),
            label: 'Graph',
          ),
        ],
        currentIndex: _selectedIndex,
        selectedItemColor: Colors.pinkAccent[400],
        unselectedItemColor: Colors.white,
        onTap: _onItemTapped,
      ),
    );
  }
}
