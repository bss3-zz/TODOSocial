// To control the modal showing up and fading
$(document).ready(function(){
    $('.modal-trigger.todo-delete').leanModal({
          ready: function(e) {
            $('#delete-type').text('todo list');
          }, // Callback for Modal open
        }
    );

    $('.modal-trigger.todo-edit').leanModal({
          ready: function(e) {
            $('#todo-modal-title').text('Edit Todo');
          }, // Callback for Modal open
        }
    );

    $('.modal-trigger.todo-create').leanModal({
          ready: function(e) {
            $('#todo-modal-title').text('Create Todo');
          }, // Callback for Modal open
        }
    );

    $('.modal-trigger.task-delete').leanModal({
          ready: function(e) {
            $('#delete-type').text('task');
          }, // Callback for Modal open
        }
    );

    $('.modal-trigger.task-edit').leanModal({
          ready: function(e) {
            $('#task-modal-title').text('Edit Task');
          }, // Callback for Modal open
        }
    );

    $('.modal-trigger.task-create').leanModal({
          ready: function(e) {
            $('#task-modal-title').text('Create Task');
          }, // Callback for Modal open
        }
    );

    $('.modal-trigger.comment-delete').leanModal({
          ready: function(e) {
            $('#delete-type').text('comment');
          }, // Callback for Modal open
        }
    );

    // To control the datepicker
    $('.datepicker').pickadate({

    });
});