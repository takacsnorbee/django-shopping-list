$(function() {
    setFooterDate();
    initAddButtonClickEvent();
    initDeleteListButtonClickEvent();
    initSaveNewListButtonClickEvent();
});

function setFooterDate() {
    $('#footerDate').text(new Date().getFullYear());
}

function initAddButtonClickEvent() {
    $('#addNewListItem').click(function(){
        let newItem = $('#newItem').val();
        if (newItem.includes(';')) {
            alert('";" character is not enable')
        } else {
            if (newItem.length > 2) {
                $('#list').append('<li>'+newItem+'</li>');
                let tempString = $('#saveThisItems').val()
                if (tempString.length < 1) {
                    tempString = $('#saveThisItems').val() + newItem;
                } else {
                    tempString = $('#saveThisItems').val() + '; ' + newItem;
                }
                $('#saveThisItems').val(tempString)
                $('#newItem').val('');
            } else {
                alert('The item name is too short. Pls type in at least 3 characters.')
            }
        }
        
    })
}

function initDeleteListButtonClickEvent() {
    $('.deleteListBtn').click(function(){
        let clickedId = $(this).attr('list-id-attr');
        $('#delByThisId').val(clickedId);
        $('#delThisListBtn').trigger("click");
    })
}

function initSaveNewListButtonClickEvent() {
    $('#saveNewList').click(function(e) {
        e.preventDefault()
        let listNameField = $('#listname').val();
        if (listNameField.length > 0) {
            $('#saveNewListSubmitBtn').trigger('click');
        } else {
            alert('List name field must be filled. At least 1 character required')
        }
        
    })
}

// function initDataToJavaScript() {
//     let fetchData = $('#vueapp1').attr('data-to-js')
//     if (fetchData != undefined || fetchData != null) {
//         let data = JSON.parse(fetchData);
//         viewListItemsVue.dataFromBackend = data; 
//     }
// }

// let viewListItemsVue = new Vue({
//     el: '#vueapp1',
//     data: {
//         dataFromBackend: '',
//     },
//     updated() {
//         console.log('yes')
//     },
//     beforeupdate() {
//         console.log('beforeupdate')
//     }
// })

// function initDataToJavaScript() {
//     let dataArray = []
//     let data = document.getElementsByClassName('userslistelement')

//     for (let i = 0; i < data.length; i++) {
//         dataArray.push(data[i].getAttribute('data-js-vars'))
//     }
//     dataArrayFromViewListItems = dataArray
// }

// function initDeleteButtonClickEvent() {
//     $('.deleteListItem').click(function() {
//         let indexOfElement = $(this).attr('index-of-elem');
//         dataArrayFromViewListItems.splice(indexOfElement, 1);
//         $(this).parents('li').remove();
//     })
// }

