/*jshint node:true*/
/* global require, module */
var EmberApp = require('ember-cli/lib/broccoli/ember-app');

module.exports = function(defaults) {
  var app = new EmberApp(defaults, {
    fingerprint:{
    enabled:true,
		prepend:"static/",
    exclude: [
      'images/layers-2x.png',
      'images/layers.png',
      'images/marker-icon-2x.png',
      'images/marker-icon.png',
      'images/marker-shadow.png'
    ]
    }
    // Add options here
  });


  app.import('bower_components/d3/d3.js');
  app.import('bower_components/topojson/topojson.js');


  return app.toTree();
};
