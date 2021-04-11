import { TestBed } from '@angular/core/testing';

import { ChooseLanguageService } from './choose-language.service';

describe('ChooseLanguageService', () => {
  let service: ChooseLanguageService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ChooseLanguageService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
