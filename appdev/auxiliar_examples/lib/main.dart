import 'package:auxiliar_examples/default/default.dart';
import 'package:flutter/material.dart';

import 'menu/menu.dart';

void main() {
  const String exemploId = "menu";
  switch (exemploId) {
    case "menu":
      runApp(const Menu());
      return;
    default:
      runApp(const Default());
      return;
  }
}
