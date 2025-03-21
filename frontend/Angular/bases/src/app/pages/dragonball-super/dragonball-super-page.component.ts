import { NgClass } from "@angular/common";
import { ChangeDetectionStrategy, Component, computed, signal, inject } from "@angular/core";
import { CharacterListComponent } from "../../components/dragonball/character-list/character-list.component";
import { CharacterAddComponent } from "../../components/dragonball/character-add/character-add.component";
import { DragonBallService } from "../../services/dragonball.services";

@Component({
    templateUrl: './dragonball-super-page.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
    selector: 'dragonball-super',
    imports: [CharacterListComponent, CharacterAddComponent],
})
export class DragonBallSuperPageComponent{
    // constructor(
    //     public dragonBallService: DragonBallService
    // ){
    // }
    public dragonBallService =  inject(DragonBallService);

    // characters = signal<Character[]>([
    //     {id: 1, name: "Goku", power: 9001},
    //     {id: 2, name: "Veggeta", power: 3000},
    // ]);

    // addCharacter(character:Character){
    //     this.characters.update(
    //         list => [...list, character]
    //     )
    // }



}