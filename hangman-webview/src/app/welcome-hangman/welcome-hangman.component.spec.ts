import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WelcomeHangmanComponent } from './welcome-hangman.component';

describe('WelcomeHangmanComponent', () => {
  let component: WelcomeHangmanComponent;
  let fixture: ComponentFixture<WelcomeHangmanComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WelcomeHangmanComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(WelcomeHangmanComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
