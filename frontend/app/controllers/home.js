import Ember from 'ember';
const {Controller,$} = Ember;

export default Controller.extend({
  object:null,
  url: null,
  actions:{

    /**
     *
     * /api/search?name="restaurant"
     *  @param {String} name business name
     *  @return {String} Object
     *  JSON.parse(Object) => business JSON object
     */
    searchRestaurant:function(){
      console.log("Searching");

      const self = this;
      let url = this.get('url').split("/");
      url = url[url.length-1];

      $.ajax({
        url: 'http://localhost:8000/search?name='+ url,
        type: 'GET'
      })
      .then((data)=>{
        let jdata = JSON.parse(data);
        console.log(jdata);
        self.set('object',jdata);
      });
    }

  }
});
