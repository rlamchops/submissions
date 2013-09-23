YUI.add('pvwatts-widget', function(Y) {

  var PvWatts = Y.namespace('Solaire.Widget').PvWatts = Y.Base.create('PvWatts', Y.Widget, [], {

    initializer: function() {
      var fields = [{id:'system_size', text:'System Size'}, {id:'track_mode', text:'Tracking'}, 
        {id:'derate', text:'DC-to-AC Derate Factor'}, {id:'tilt', text:'Tilt'}, {id:'azimuth', text:'Azimuth'}];
      this.set('fields', fields);  
    },

    destructor: function() {
      this._input.remove();
      this._submit.remove();
    },

    renderUI: function() {
      this._renderInputNode();
      this._renderSubmitButton();
    },

    bindUI: function() {
      this._submit.on('click', this._onInputSubmit, this);
    },

    syncUI: function() {

    },

    _createResultsWidget: function() {
      this.results = {};
    },

    _renderInputNode: function() {
      var cb = this.get('contentBox');
      var input = cb.one('.system-info');

      if(!input) {
        var fields = this.get('fields');
        input = Y.Node.create('<div class=system-info></div>');

        Y.Array.each(fields, function(field) {
          input.appendChild('<div class=label>' + field.text + '</div><input class=input id=' + field.id + ' type=text></br>');
        }, this);

        cb.appendChild(input);
      }

      this._input = input;
    },

    _renderSubmitButton: function() {
      var cb = this.get('contentBox');
      var submit = cb.one('.submit-info');

      if(!submit) {
        submit = Y.Node.create('<input class=submit-info type=submit>');
        cb.appendChild(submit);
      }

      this._submit = submit;
    },

    _onInputSubmit: function(e) {
      var children = this._input.all('input');
      var lat = window.location.search.split('&')[0].split('?').join('');
      var lon = window.location.search.split('&')[1];
      var parameters = 'api_key=' + this.get('apiKey') + '&callback={callback}' 
        + '&' + lat + '&' + lon + '&'; 

      children.each(function(child) {
        parameters += '&' + child.get('id') + '=' + child.get('value');
      }, this);

      var requestUri = this.get('uriBase') + '?' + parameters;
      Y.jsonp(requestUri, Y.bind(this._handleJsonp, this));
    },

    _handleJsonp: function(response) {
      if(response.errors.length === 0) {
        this.get('contentBox').addClass('invisible');
        console.log(response);
      }
    } 

  }, {
    CSS_PREFIX: 'pvwatts',
    ATTRS: {
      uriBase: {
        value: 'http://developer.nrel.gov/api/pvwatts/v4.json'
      },
      apiKey: {
        value: '6a1fa009180f6151ff6587fc63904374da7d36eb'
      },
      fields: {
        value: []
      },
      data: {
        value: {}
      },
      address: {
        value: {
          lat: '',
          lon: ''
        }
      }
    }
  });
}, '1.0', {
  requires: [
    'base',
    'node',
    'widget',
    'event',
    'jsonp',
    'jsonp-url'
  ]
});