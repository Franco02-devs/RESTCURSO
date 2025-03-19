import { UpperCasePipe } from "@angular/common";
import { ChangeDetectionStrategy, Component, computed, signal } from "@angular/core";

@Component({
    templateUrl: './hero-page.component.html',
    imports:[UpperCasePipe],
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class HeroPageComponent{
    name = signal('Ironman')
    age = signal(45)
    heroDescription = computed(() =>{
        const description = `${ this.name() } - ${ this.age() }`;
        return description
    })
    capitalizedName = computed(() =>{
        const upperName = this.name().toUpperCase();
        return upperName
    })
    changeHero(){
        this.name.set("Spiderman")
        this.age.set(22)
    }
    resetForm(){
        this.name.set("Ironman")
        this.age.set(45)
    }
    changeAge(){
        this.age.set(60)
    }
    toUpper(){
        return this.name().toUpperCase()
    }

}