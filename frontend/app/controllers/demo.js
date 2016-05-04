import Ember from 'ember';
const {Controller,computed,Object} = Ember;


export default Controller.extend({
  first: computed('model.[]',function(){
    return this.get('model').get('firstObject');
  })
});
