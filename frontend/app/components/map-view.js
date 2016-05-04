import Ember from 'ember';
const {Component,computed} = Ember;

const map =  Component.extend({
  score:{
    major_score:0,
    minor_score:0,
    serve_score:0
  },
  zoom: 10,
  markers: computed('model.@each.{major_violation_score,serve_violation_score,minor_violation_score','score.{major_score,minor_score,serve_score}',function(){
    const list = this.get('model');
    console.log(list);
    const major_score = this.get('score.major_score');
    const serve_score = this.get('score.serve_score');
    const minor_score = this.get('score.minor_score');
    if ((major_score == 0) && (serve_score == 0) && (minor_score == 0)){
      return list;
    };
    const filtered =  list.filter(function(item){
      let cond = item.get('minor_violation_score') >= minor_score &&
        item.get('major_violation_score') >= major_score &&
        item.get('serve_violation_score') >= serve_score;
      console.log(cond);
      return cond;
    });

    return filtered;
  }),

  actions: {
    updateCenter(e) {
      let center = e.target.getCenter();
      this.set('lat', center.lat);
      this.set('lng', center.lng);
    }
  },

  didReceiveAttrs(){
    this._super(...arguments);
  }
});


export default map;
