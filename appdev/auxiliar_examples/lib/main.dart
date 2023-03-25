import 'package:flutter/material.dart';

import 'package:auxiliar_examples/default/default.dart';
import 'package:auxiliar_examples/infinite_list/infinite_list.dart';
import 'package:auxiliar_examples/menu/menu.dart';

void main() {
  const String exemploId = "infinite";
  switch (exemploId) {
    case "infinite":
      runApp(const InfiniteList());
      return;
    case "menu":
      runApp(const Menu());
      return;
    default:
      runApp(const Default());
      return;
  }
}
