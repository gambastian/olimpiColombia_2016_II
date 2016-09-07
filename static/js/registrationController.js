(function () {
    'use strict';

    var RegistrationCrtl = function ($rootScope, $scope, $location, registrationService) {
        $scope.error = false;
        $scope.submitForm = function () {
            var res = registrationService.login($scope.form).then(function (data) {
                if(data.mensaje =='ok')
                {
                    $rootScope.authenticated = true;
                	$location.url("/deportes");
                }else{
                    console.log('Ocurrio un error:' + data);
                    $scope.error = true;
                }
            }, function (response) {
                $scope.error = true;
                console.log('Error: ' + response);
            })
        }

    };

    angular.module('olimpicolombia.controllers').controller('RegistrationCrtl', ['$rootScope', '$scope', '$location', 'registrationService', RegistrationCrtl]);
}());