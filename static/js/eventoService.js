(function () {
    'use strict';

    var EventoSvc = function ($http) {
        var eventoService = {
            list: function (deportistaId) {
                var promise = $http.get('/api/evento/' + deportistaId, {})
                    .then(function (response) {
                        return response.data;
                    });
                return promise;
            }
        };

        return eventoService;
    };

    angular.module('olimpicolombia.services').factory('eventoService', ['$http', EventoSvc]);
}());
