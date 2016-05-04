import DS from 'ember-data';

const {attr} = DS;

let business = DS.Model.extend({
  name: attr(),
  major_violation_score: attr(),
  serve_violation_score: attr(),
  minor_violation_score: attr(),
  cateogires: attr(),
  latitude: attr(),
  longitude: attr()
});

export default business;
