import 'package:flutter/material.dart';
import 'package:webfeed/webfeed.dart';
import 'package:http/http.dart' as http;
import 'package:url_launcher/url_launcher.dart';
import 'package:intl/intl.dart';


class RSSFeed extends StatefulWidget{
  const RSSFeed(this.strUrl, {super.key});
  final String strUrl;
  final String title = 'RSS Feed';
  @override
  RSSFeedState createState() => RSSFeedState();
}

class RSSFeedState extends State<RSSFeed> {
  late Uri FEED_URL;
  RssFeed? _feed;
  late String _title;
  static const String loadingFeedMsg = 'Loading Feed...';
  static const String feedLoadErrorMsg = 'Error Loading Feed';
  static const String feedOpenErrorMsg = 'Error Opening Feed';
  late GlobalKey<RefreshIndicatorState> _refreshKey;


  urlConv(string){
    setState(() {
      FEED_URL = Uri.parse(string);
    });
  }

  updateTitle(title){
    setState(() {
      _title = title;
    });
  }

  updateFeed(feed){
    setState(() {
      _feed = feed;
    });
  }

  load() async{
    updateTitle(loadingFeedMsg);
    loadFeed().then((result){
      if(null == result || result.toString().isEmpty){
        updateTitle(feedLoadErrorMsg);
        return;
      }
      updateFeed(result);
      updateTitle(_feed?.title);
    });

  }

  Future<void> openFeed(Uri url) async{
    if(await launchUrl(url, mode: LaunchMode.externalApplication)){
      //await launchUrl(url);
      return;
    }
    updateTitle(feedOpenErrorMsg);
  }

  Future<RssFeed?> loadFeed() async {
    try{
      final client = http.Client();
      final response = await client.get(FEED_URL);
      return RssFeed.parse(response.body);
    } catch(e){
      //
    }
    return null;
  }

  @override
  void initState() {
    super.initState();
    urlConv(widget.strUrl);
    _refreshKey =  GlobalKey<RefreshIndicatorState>();
    updateTitle(widget.title);
    load();
  }

  title(title) {
    return Text(
      title,
      style: const TextStyle(fontSize: 18.0, fontWeight: FontWeight.w500),
      maxLines: 2,
      overflow: TextOverflow.ellipsis,
    );
  }
  subtitle(subTitle) {
    return Text(
      subTitle,
      style: const TextStyle(fontSize: 14.0, fontWeight: FontWeight.w100),
      maxLines: 1,
      overflow: TextOverflow.ellipsis,
    );
  }

  rightIcon(){
    return const Icon(
      Icons.keyboard_arrow_right,
      color: Colors.grey,
      size: 30,
    );
  }
  list() {
    return ListView.builder(
      itemCount: _feed?.items?.length,
      itemBuilder: (BuildContext context, int index) {
        final item = _feed?.items?[index];
        return ListTile(
          title: title(item?.title),
          subtitle: subtitle(DateFormat('dd-MM-yyyy – kk:mm').format(item!.pubDate as DateTime)),
          trailing: rightIcon(),
          contentPadding: const EdgeInsets.all(5.0),
          onTap: () => openFeed(Uri.parse(item.link as String)),
        );

      },
    );
  }

  isFeedEmpty(){
    return null == _feed || null == _feed?.items;
  }

  body() {
    return isFeedEmpty()
        ? const Center(
      child: CircularProgressIndicator(),
    )
        : RefreshIndicator(
      key: _refreshKey,
      child: list(),
      onRefresh: () =>  load(),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(_title),
      ),
      body: body(),
    );
  }
}