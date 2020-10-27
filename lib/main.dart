// Copyright 2017, Paul DeMarco.
// All rights reserved. Use of this source code is governed by a
// BSD-style license that can be found in the LICENSE file.

import 'package:flutter/material.dart';
import 'package:glove_reader/components/menu/menu.dart';
import 'package:glove_reader/themes/style.dart';

void main() {
  runApp(FlutterBlueApp());
}

class FlutterBlueApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: appTheme(),
      title: 'Glove Reader',
      home: Menu(),
    );
  }
}
