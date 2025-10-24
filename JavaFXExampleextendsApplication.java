importjavafx.application.Application; import javafx.scene.Scene;
importjavafx.scene.control.Button; import javafx.stage.Stage;
importjavafx.scene.layout.StackPane;
publicclassJavaFXExampleextendsApplication{
//applicationstartshere 
@Override
publicvoidstart(Stages)throwsException{
//createbutton
Buttonbtn=newButton("SampleButton");
//createstackpane
StackPaner=newStackPane();
//addbuttontostackpane r.getChildren().add(btn);
//createscene
Scenesc=newScene(r,500,300);
//set title for the stage s.setTitle("JavaFXExample");
//setsceneforthestage s.setScene(sc);
//displaytheresult s.show();
}
//mainmethod
publicstaticvoidmain(String[]args)
{
launch(args);
}
}
